from dataclasses import dataclass
from dominion.base import CardShapedThing, Cost, Pile
from dominion.card_shaped_things import (
    EVENTS,
    KINGDOM_PILES,
    LANDMARKS,
    PROPHECIES,
)
import random
from typing import Callable
import time

@dataclass
class GameSettings:
    seed: int
    sets: set[str]

@dataclass
class Game:
    settings: GameSettings
    kingdom_piles: list[Pile]
    landscapes: list[CardShapedThing]

def no_first_editions(card_shaped_thing: CardShapedThing) -> bool:
    edition = card_shaped_thing.set.edition
    return edition is None or edition != '1E'

def pick_sets(card_shaped_thing: CardShapedThing, sets: set[str]) -> bool:
    return card_shaped_thing.set.name in sets

def card_shaped_thing_comparison_key(card_shaped_thing: CardShapedThing) -> tuple[Cost, str]:
    return (card_shaped_thing.cost, card_shaped_thing.name)

def pile_comparison_key(pile: Pile) -> tuple[Cost, str]:
    top_card = pile.cards[0]
    return card_shaped_thing_comparison_key(top_card)

def generate_kingdom(settings: GameSettings, exclude_names: set[str]|None=None) -> Game:
    random.seed(settings.seed)

    if exclude_names is None:
        exclude_names = set()

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

    tournament_exclude_events = {
        'Continue',
        'Foresight',
        'Kintsugi',
        'Receive Tribute',
    }

    adventure_token_cards = {
        'Bridge Troll',
        'Giant',
        'Peasant',
        'Ranger',
        'Relic',
    }

    adventure_token_events = {
        'Borrow',
        'Ferry',
        'Plan',
        'Pilgrimage',
        'Ball',
        'Raid',
        'Seaway',
        'Lost Arts',
        'Training',
        'Pathfinding',
    }

    kingdom_rules: list[Callable[[CardShapedThing], bool]] = [
        no_first_editions,
        lambda c: pick_sets(c, settings.sets),
        lambda c: c.name not in tournament_exclude_cards and c.name not in adventure_token_cards,
        lambda c: len(c.types.intersection({'Doom', 'Fate', 'Reserve'})) == 0,
    ]

    event_rules: list[Callable[[CardShapedThing], bool]] = [
        lambda e: pick_sets(e, settings.sets),
        lambda e: e.name not in tournament_exclude_events and e.name not in adventure_token_events,
    ]

    landmark_rules: list[Callable[[CardShapedThing], bool]] = [
        lambda c: pick_sets(c, settings.sets),
    ]

    prophecy_rules: list[Callable[[CardShapedThing], bool]] = [
    ]

    kingdom_pile_options: list[Pile] = []
    for pile in KINGDOM_PILES:
        if pile.name not in exclude_names and all(rule(card) for rule in kingdom_rules for card in pile.cards):
            kingdom_pile_options.append(pile)

    assert len(kingdom_pile_options) >= 10, f'options: {", ".join(pile.name for pile in kingdom_pile_options)}'

    random.shuffle(kingdom_pile_options)
    kingdom_piles = kingdom_pile_options[:10]
    kingdom_piles.sort(key=lambda pile: pile_comparison_key(pile))

    landscapes: list[CardShapedThing] = []

    events_options: list[CardShapedThing] = []
    for event in EVENTS:
        if event.name not in exclude_names and all(rule(event) for rule in event_rules):
            events_options.append(event)
    random.shuffle(events_options)
    num_events = random.randint(0, 2)
    landscapes.extend(events_options[:num_events])

    landmarks_options: list[CardShapedThing] = []
    for landmark in LANDMARKS:
        if landmark.name not in exclude_names and all(rule(landmark) for rule in landmark_rules):
            landmarks_options.append(landmark)
    random.shuffle(landmarks_options)
    num_landmarks = random.randint(0, 2)
    landscapes.extend(landmarks_options[:num_landmarks])

    if any('Omen' in card.types for pile in kingdom_piles for card in pile.cards):
        prophecies_options: list[CardShapedThing] = []
        for prophecy in PROPHECIES:
            if prophecy.name not in exclude_names and all(rule(prophecy) for rule in prophecy_rules):
                prophecies_options.append(prophecy)
        landscapes.append(random.choice(prophecies_options))

    landscapes.sort(key=lambda landscape: card_shaped_thing_comparison_key(landscape))

    game = Game(settings, kingdom_piles, landscapes)
    return game

def write_html(games: list[Game], filename: str) -> None:
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
.seed {
  text-align: center;
  font-size: 14pt;
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
            f.write(f'<div class="seed"><p>seed: {game.settings.seed}</p></div>\n')
            ordered_piles = game.kingdom_piles[5:] + game.kingdom_piles[:5]
            f.write('<div class="kingdom_piles">\n')
            for pile in ordered_piles:
                top_card = pile.cards[0]
                link = top_card.link
                image = top_card.image
                f.write(f'  <div><a href="{link}"><img alt="{pile.name}" src="{image}"/></a></div>\n')
            f.write('</div>\n')

            f.write('<div class="landscapes">\n')
            for landscape in game.landscapes:
                link = landscape.link
                image = landscape.image
                f.write(f'  <div><a href="{link}"><img alt="{landscape.name}" src="{image}"/></a></div>\n')
            f.write('</div>\n')

        f.write('\n</body>\n</html>\n')

def main() -> None:
    game_settings = [
        GameSettings(1768670846218130800, {'Base', 'Adventures'}),
        GameSettings(time.time_ns(), {'Intrigue', 'Prosperity'}),
        GameSettings(time.time_ns(), {'Seaside', 'Rising Sun'}),
        GameSettings(time.time_ns(), {'Alchemy', 'Promo'}),
        GameSettings(time.time_ns(), {'Empires', 'Nocturne'}),
        GameSettings(time.time_ns(), {'Cornucopia & Guilds'}),
    ]

    game_num = 1
    games: list[Game] = []
    exclude_names: set[str] = set()
    for settings in game_settings:
        game = generate_kingdom(settings, exclude_names)
        games.append(game)

        set_names = ', '.join(settings.sets)
        print(f'Game {game_num} ({set_names}):')
        for pile in game.kingdom_piles:
            costs = '/'.join(str(card.cost) for card in pile.cards)
            print(f"{pile.name} {costs}")
        print()

        exclude_names |= set(pile.name for pile in game.kingdom_piles)
        exclude_names |= set(landscape.name for landscape in game.landscapes)

        game_num += 1

    write_html(games, 'games.html')

if __name__ == '__main__':
    main()
