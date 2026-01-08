from dataclasses import dataclass
import json
import random
from typing import Any, Callable
import time

@dataclass
class GameSettings:
    seed: int
    sets: set[str]

@dataclass
class Game:
    kingdom_piles: list[dict[str, Any]]
    events: list[dict[str, Any]]

def no_first_editions(card: dict[str, Any]) -> bool:
    edition = card['Set']['Edition']
    return edition is None or edition == '2E'

def pick_sets(card: dict[str, Any], sets: set[str]) -> bool:
    return card['Set']['Name'] in sets

def card_shaped_thing_comparison_key(name: str, cards: dict[str, Any]) -> tuple[int, int, int, str]:
    card_shaped_thing = cards['CardShapedThings'][name]

    key = [0, 0, 0, card_shaped_thing['Name']]

    cost_str = card_shaped_thing['Cost']
    cost_split = cost_str.split()
    for part in cost_split:
        if part[0] == '$':
            s = part[1:]
            if s[-1] in {'*', '+'}:
                s = s[:-1]
            key[0] = int(s)
        elif part[-1] == 'P':
            key[1] = 1 if len(part) == 1 else int(part[:-1])
        elif part[-1] == 'D':
            key[2] = 1 if len(part) == 1 else int(part[:-1])
        else:
            assert False, f'Unknown cost part: {part}'

    return tuple(key)

def pile_comparison_key(pile: dict[str, Any], cards: dict[str, Any]) -> tuple[int, int, int, str]:
    top_card_name = pile['Cards'][0]
    return card_shaped_thing_comparison_key(top_card_name, cards)

def generate_kingdom(cards: dict[str, Any], settings: GameSettings, exclude_piles: set[str]|None=None) -> Game:
    random.seed(settings.seed)

    if exclude_piles is None:
        exclude_piles = set()

    tournament_exclude_cards = {
        'Bureaucrat',          # not exciting
        'Militia',             # slows down games
        'Masquerade',          # slows down games
        'Patrol',              # slows down games
        'Secret Passage',      # slows down games
        'Swindler',            # slows down games and can be annoying
        'Torturer',            # slows down games and can be annoying
        'Lookout',             # slows down games
        "Philosopher's Stone", # slows down games
        'Possession',          # slows down games and can be annoying
        'Scrying Pool',        # slows down games
        'Clerk',               # slows down games
        'Rabble',              # slows down games
        'Vault',               # slows down games
        'Advisor',             # slows down games
        'Footpad',             # slows down games
        'Jester',              # slows down games
        'Giant',               # slows down games and can be annoying
        'Haunted Woods',       # slows down games
        'Ninja',               # slows down games
        'Black Market',        # setup is too complex
        'Envoy',               # slows down games
    }

    adventure_token_cards = {
        'Bridge Troll',
        'Giant',
        'Peasant',
        'Ranger',
        'Relic',
    }

    kingdom_rules: list[Callable[[dict[str, Any]], bool]] = [
        no_first_editions,
        lambda c: pick_sets(c, settings.sets),
        lambda c: c['Name'] not in tournament_exclude_cards and c['Name'] not in adventure_token_cards,
        lambda c: len(set(c['Types']).intersection({'Doom', 'Fate', 'Reserve'})) == 0,
    ]

    event_rules: list[Callable[[dict[str, Any]], bool]] = [
        lambda c: pick_sets(c, settings.sets),
    ]

    kingdom_pile_options = []
    for pile in cards['KingdomPiles']:
        if pile['Name'] not in exclude_piles and all(rule(cards['CardShapedThings'][card_name]) for rule in kingdom_rules for card_name in pile['Cards']):
            kingdom_pile_options.append(pile)

    assert len(kingdom_pile_options) >= 10

    random.shuffle(kingdom_pile_options)
    kingdom_piles = kingdom_pile_options[:10]
    kingdom_piles.sort(key=lambda pile: pile_comparison_key(pile, cards))

    events_options = []
    for event_name in cards['Events']:
        if event_name not in exclude_piles and all(rule(cards['CardShapedThings'][event_name]) for rule in event_rules):
            events_options.append(event_name)

    random.shuffle(events_options)
    num_events = random.randint(0, 2)
    events = events_options[:num_events]
    events.sort(key=lambda event: card_shaped_thing_comparison_key(event, cards))

    game = Game(kingdom_piles, events)
    return game

def write_html(games: list[Game], cards: dict[str, Any], filename: str) -> None:
    with open(filename, 'w', encoding='utf8') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
<title>Dominion Games</title>
<style>
body {
  background-image: url(1024px-BaseArt.jpg);
  background-attachment: fixed;
}
h1 {
  text-align: center;
  font-family: "Times New Roman";
  font-size: 28pt;
  font-variant: small-caps;
}
.kingdom_piles {
  display: grid;
  grid-template-columns: 210px 210px 210px 210px 210px;
  place-content: center;
}
.kingdom_piles div {
  padding: 10px;
}
.landscapes {
  display: grid;
  grid-template-columns: auto auto;
  place-content: center;
}
.landscapes div {
  padding: 10px;
}
</style>
</head>

<body>
''')

        for i, game in enumerate(games):
            f.write(f'\n<h1><img src="./list_of_cards_files/28px-VP.png"/>Game {i + 1}<img src="./list_of_cards_files/28px-VP.png"/></h1>\n\n')
            ordered_piles = game.kingdom_piles[5:] + game.kingdom_piles[:5]
            f.write('<div class="kingdom_piles">\n')
            for pile in ordered_piles:
                pile_name = pile['Name']
                top_card_name = pile['Cards'][0]
                top_card = cards['CardShapedThings'][top_card_name]
                link = top_card['Link']
                image = top_card['Image']
                f.write(f'  <div><a href="{link}"><img alt="{pile_name}" src="{image}"/></a></div>\n')
            f.write('</div>\n')

            f.write('<div class="landscapes">\n')
            for event_name in game.events:
                event = cards['CardShapedThings'][event_name]
                link = event['Link']
                image = event['Image']
                f.write(f'  <div><a href="{link}"><img alt="{event_name}" src="{image}"/></a></div>\n')
            f.write('</div>\n')

        f.write('\n</body>\n</html>\n')

def main() -> None:
    cards_list_filename = 'dominion_cards.json'
    with open(cards_list_filename, 'r', encoding='utf8') as f:
        cards: dict[str, Any] = json.load(f)

    game_settings = [
        GameSettings(time.time_ns(), {'Base', 'Adventures'}),
        GameSettings(time.time_ns(), {'Intrigue', 'Prosperity'}),
        GameSettings(time.time_ns(), {'Seaside', 'Rising Sun'}),
        GameSettings(time.time_ns(), {'Alchemy', 'Promo'}),
        GameSettings(time.time_ns(), {'Empires', 'Nocturne'}),
    ]

    game_num = 1
    games: list[Game] = []
    exclude_piles: set[str] = set()
    for settings in game_settings:
        game = generate_kingdom(cards, settings, exclude_piles)
        games.append(game)

        set_names = ', '.join(settings.sets)
        print(f'Game {game_num} ({set_names}):')
        for pile in game.kingdom_piles:
            costs = '/'.join(cards['CardShapedThings'][card_name]['Cost'] for card_name in pile['Cards'])
            print(f"{pile['Name']} {costs}")
        print()

        exclude_piles |= set(pile['Name'] for pile in game.kingdom_piles)

        game_num += 1

    write_html(games, cards, 'games.html')

if __name__ == '__main__':
    main()
