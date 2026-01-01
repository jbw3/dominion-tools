from dataclasses import dataclass
import json
import random
from typing import Any, Callable

@dataclass
class Game:
    kingdom_cards: list[dict[str, Any]]

def no_first_editions(card: dict[str, Any]) -> bool:
    edition = card['Set']['Edition']
    return edition is None or edition == '2E'

def pick_expansions(card: dict[str, Any], expansions: set[str]) -> bool:
    return card['Set']['Name'] in expansions

def card_comparison_key(card: dict[str, Any]) -> tuple[int, int, int, str]:
    key = [0, 0, 0, card['Name']]

    cost_str = card['Cost']
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

def generate_kingdom(cards: dict[str, Any]) -> Game:
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
        lambda c: pick_expansions(c, {'Cornucopia & Guilds'}),
        lambda c: c['Name'] not in tournament_exclude_cards and c['Name'] not in adventure_token_cards,
    ]

    kingdom_card_options = [
        card
        for card in cards['Kingdom']
        if all(rule(card) for rule in kingdom_rules)
    ]
    assert len(kingdom_card_options) >= 10

    random.shuffle(kingdom_card_options)

    kingdom_cards = kingdom_card_options[:10]

    kingdom_cards.sort(key=card_comparison_key)

    game = Game(kingdom_cards)
    return game

def main() -> None:
    cards_list_filename = 'dominion_cards.json'
    with open(cards_list_filename, 'r', encoding='utf8') as f:
        cards: dict[str, Any] = json.load(f)

    game = generate_kingdom(cards)
    for card in game.kingdom_cards:
        print(f"{card['Name']} {card['Cost']}")

if __name__ == '__main__':
    main()
