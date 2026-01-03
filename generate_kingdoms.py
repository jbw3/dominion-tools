from dataclasses import dataclass
import json
import random
from typing import Any, Callable

@dataclass
class Game:
    kingdom_piles: list[dict[str, Any]]

def no_first_editions(card: dict[str, Any]) -> bool:
    edition = card['Set']['Edition']
    return edition is None or edition == '2E'

def pick_expansions(card: dict[str, Any], expansions: set[str]) -> bool:
    return card['Set']['Name'] in expansions

def pile_comparison_key(pile: dict[str, Any], cards: dict[str, Any]) -> tuple[int, int, int, str]:
    top_card_name = pile['Cards'][0]
    top_card = cards['CardShapedThings'][top_card_name]

    key = [0, 0, 0, top_card['Name']]

    cost_str = top_card['Cost']
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

def generate_kingdom(cards: dict[str, Any], expansions: set[str], exclude_piles: set[str]|None=None) -> Game:
    if exclude_piles is None:
        exclude_piles = set()

    tournament_exclude_cards = {
        'Bureaucrat',          # not exciting
        'Militia',             # slows down games
        'Secret Passage',      # slows down games
        'Swindler',            # slows down games and can be annoying
        'Torturer',            # slows down games and can be annoying
        'Lookout',             # slows down games
        "Philosopher's Stone", # slows down games
        'Possession',          # slows down games and can be annoying
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
        lambda c: pick_expansions(c, expansions),
        lambda c: c['Name'] not in tournament_exclude_cards and c['Name'] not in adventure_token_cards,
    ]

    kingdom_pile_options = []
    for pile in cards['KingdomPiles']:
        if pile['Name'] not in exclude_piles and all(rule(cards['CardShapedThings'][card_name]) for rule in kingdom_rules for card_name in pile['Cards']):
            kingdom_pile_options.append(pile)

    assert len(kingdom_pile_options) >= 10

    random.shuffle(kingdom_pile_options)

    kingdom_piles = kingdom_pile_options[:10]

    kingdom_piles.sort(key=lambda pile: pile_comparison_key(pile, cards))

    game = Game(kingdom_piles)
    return game

def write_html(games: list[Game], filename: str) -> None:
    with open(filename, 'w', encoding='utf8') as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
<title>Dominion Games</title>
<style>
.cards_row {
  display: grid;
  grid-template-columns: 210px 210px 210px 210px 210px;
}
.cards_row div {
  padding: 10px;
}
</style>
</head>

<body>
''')

        for i, game in enumerate(games):
            f.write(f'\n<h1>Game {i + 1}</h1>\n\n')
            ordered_piles = game.kingdom_piles[5:] + game.kingdom_piles[:5]
            f.write('<div class="cards_row">\n')
            for pile in ordered_piles:
                pile_name = pile['Name']
                top_card = pile['Cards'][0]
                img_path = f'./list_of_cards_files/200px-{top_card}.jpg'.replace(' ', '_')
                # f.write(f'  <div>{pile_name}</div>\n')
                f.write(f'  <div><img alt="{pile_name}" src="{img_path}"/></div>\n')
            f.write('</div>\n')

        f.write('</body>\n</html>\n')

def main() -> None:
    cards_list_filename = 'dominion_cards.json'
    with open(cards_list_filename, 'r', encoding='utf8') as f:
        cards: dict[str, Any] = json.load(f)

    game_expansions = [
        ['Base', 'Adventures'],
        ['Intrigue', 'Prosperity'],
        ['Seaside', 'Rising Sun'],
        ['Empires', 'Nocturne'],
    ]

    game_num = 1
    games: list[Game] = []
    exclude_piles: set[str] = set()
    for expansions in game_expansions:
        game = generate_kingdom(cards, set(expansions), exclude_piles)
        games.append(game)

        expansion_names = ', '.join(expansions)
        print(f'Game {game_num} ({expansion_names}):')
        for pile in game.kingdom_piles:
            costs = '/'.join(cards['CardShapedThings'][card_name]['Cost'] for card_name in pile['Cards'])
            print(f"{pile['Name']} {costs}")
        print()

        exclude_piles |= set(pile['Name'] for pile in game.kingdom_piles)

        game_num += 1

    write_html(games, 'games.html')

if __name__ == '__main__':
    main()
