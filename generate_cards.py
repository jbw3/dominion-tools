from dataclasses import dataclass
from enum import IntEnum
import json
import urllib.parse

class PrimaryColor(IntEnum):
    Action = 0
    Event = 0
    Treasure = 1
    Victory = 2
    Reaction = 3
    Duration = 4
    Reserve = 5
    Curse = 6
    Shelter = 7
    Ruins = 8
    Landmark = 9
    Night = 10

PRIMARY_COLOR_MAP = {e.name: e for e in PrimaryColor}

class SecondaryColor(IntEnum):
    SAME = 0
    Action = 1
    Event = 1
    Treasure = 2
    Victory = 3
    Reaction = 4
    Duration = 5
    Reserve = 6
    Curse = 7
    Shelter = 8
    Ruins = 9
    Landmark = 10
    Night = 11

SECONDARY_COLOR_MAP = {e.name: e for e in SecondaryColor}

def primary_to_secondary(primary_color: PrimaryColor) -> SecondaryColor:
    return SecondaryColor(primary_color.value + 1)

@dataclass
class Card:
    name: str
    cost: str
    types: str
    text: str
    preview: str
    heirloom: str

def check_name(card: Card) -> None:
    name = card.name

    if name.strip() == '':
        print('Card does not have a name')
        return

    expected_name = ' '.join(part[0].upper() + part[1:].lower() for part in name.split())
    if name != expected_name:
        print(f'"{name}" expected to be "{expected_name}"')

VALID_TYPES = {
    'Action',
    'Attack',
    'Command',
    'Curse',
    'Doom',
    'Duration',
    'Fate',
    'Heirloom',
    'Night',
    'Prize',
    'Reaction',
    'Reserve',
    'Reward',
    'Shadow',
    'Shelter',
    'Spirit',
    'Traveller',
    'Treasure',
    'Victory',
    'Zombie',

    # custom types
    'Spell',
}

def check_types(card: Card) -> None:
    name = 'Card' if card.name == '' else card.name

    if card.types.strip() == '':
        print(f'{name} does not have types')
        return

    for t in card.types.split(' - '):
        if t not in VALID_TYPES:
            print(f'{name} has an invalid type "{t}"')

def check_card(card: Card) -> None:
    name = 'Card' if card.name == '' else card.name

    check_name(card)

    if card.cost.strip() == '':
        print(f'{name} does not have a cost')

    check_types(card)

    if card.text.strip() == '':
        print(f'{name} does not have text')

def create_url_string(card: Card) -> str:
    types_list = [t.strip() for t in card.types.split('-')]
    primary_color: PrimaryColor|None = None
    secondary_color: SecondaryColor|None = None
    for t in types_list:
        if (primary_color is None
        or (primary_color == PrimaryColor.Action and t == 'Duration')
        or (primary_color == PrimaryColor.Action and t == 'Reaction')):
            primary_color = PRIMARY_COLOR_MAP.get(t)
        elif ((primary_color == PrimaryColor.Treasure and t == 'Duration')
        or (primary_color == PrimaryColor.Duration and t == 'Reaction')):
            secondary_color = primary_to_secondary(primary_color)
            primary_color = PRIMARY_COLOR_MAP.get(t)
        else:
            secondary_color = SECONDARY_COLOR_MAP.get(t)

    if primary_color is None:
        primary_color = PrimaryColor.Action
    if secondary_color is None:
        secondary_color = SecondaryColor.SAME

    url = '?title=' + urllib.parse.quote(card.name)
    url += '&description=' + urllib.parse.quote(card.text)
    url += '&type=' + urllib.parse.quote(card.types)
    url += '&credit='
    url += '&creator='
    url += '&price=' + urllib.parse.quote(card.cost)
    url += '&preview=' + urllib.parse.quote(card.preview)
    url += '&type2=' + urllib.parse.quote(card.heirloom)
    url += '&color2split=18'
    url += '&boldkeys='
    url += '&picture-x=0'
    url += '&picture-y=0'
    url += '&picture-zoom=1'
    url += '&traveller=false'
    url += '&trait=false'
    url += '&picture='
    url += '&expansion=%5Blocal%20image%5D'
    url += '&custom-icon='
    url += f'&color0={primary_color.value}'
    url += f'&color1={secondary_color.value}'
    url += '&size=0'

    return url

def main() -> None:
    cards: list[Card] = []
    with open('Dominion Card Ideas - Cards.tsv', 'r', encoding='utf-8') as f:
        # read header
        f.readline()

        for line in f:
            fields = line.split('\t')
            card = Card(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5])
            cards.append(card)

    for card in cards:
        check_card(card)

    card_url_list = [create_url_string(card) for card in cards]
    with open('dominion-card-generator.json', 'w') as f:
        json.dump(card_url_list, f)

if __name__ == '__main__':
    main()
