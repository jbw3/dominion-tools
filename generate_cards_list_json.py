from html.parser import HTMLParser
import json
from pathlib import Path
from typing import Any, IO

def create_card() -> dict[str, Any]:
    return {
        'Name': '',
        'Set': {
            'Name': '',
            'Edition': None,
        },
        'Types': [],
        'Cost': '',
        'Text': '',
        'Image': '',
        'Link': '',
    }

BASE_CARD_NAMES = {
    'Copper',
    'Silver',
    'Gold',
    'Platinum',
    'Potion',
    'Curse',
    'Estate',
    'Duchy',
    'Province',
    'Colony',
}

def is_base_card(card: dict[str, Any]) -> bool:
    return card['Name'] in BASE_CARD_NAMES

def is_non_supply_card(card: dict[str, Any]) -> bool:
    for t in card['Types']:
        if t == 'Loot':
            return True

    return '(This is not in the Supply.)' in card['Text']

VALID_KINGDOM_CARD_TYPES = {
    'Action',
    'Attack',
    'Augur',
    'Castle',
    'Clash',
    'Command',
    'Doom',
    'Duration',
    'Fate',
    'Fort',
    'Gathering',
    'Knight',
    'Liaison',
    'Looter',
    'Night',
    'Odyssey',
    'Omen',
    'Reaction',
    'Reserve',
    'Shadow',
    'Townsfolk',
    'Traveller',
    'Treasure',
    'Victory',
    'Wizard',
}

def assert_kingdom_card_types(types: list[str]) -> None:
    for t in types:
        assert t in VALID_KINGDOM_CARD_TYPES, f'{t} is not a valid kingdom card type'

SPLIT_PILE_NAMES = {
    'Avanto': 'Sauna/Avanto',
    'Bustling Village': 'Settlers/Bustling Village',
    'Catapult': 'Catapult/Rocks',
    'Emporium': 'Patrician/Emporium',
    'Encampment': 'Encampment/Plunder',
    'Fortune': 'Gladiator/Fortune',
    'Gladiator': 'Gladiator/Fortune',
    'Patrician': 'Patrician/Emporium',
    'Plunder': 'Encampment/Plunder',
    'Rocks': 'Catapult/Rocks',
    'Sauna': 'Sauna/Avanto',
    'Settlers': 'Settlers/Bustling Village',
}

SPLIT_PILE_TYPES = {
    'Augur': 'Augurs',
    'Castle': 'Castles',
    'Clash': 'Clashes',
    'Fort': 'Forts',
    'Knight': 'Knights',
    'Odyssey': 'Odysseys',
    'Townsfolk': 'Townsfolk',
    'Wizard': 'Wizards',
}

def get_pile_name(card: dict[str, Any]) -> str:
    name = SPLIT_PILE_NAMES.get(card['Name'])
    if name is not None:
        return name

    for type in card['Types']:
        name = SPLIT_PILE_TYPES.get(type)
        if name is not None:
            return name

    return card['Name']

def card_comparison_key(card_name: str, cards: dict[str, Any]) -> tuple[int, int, int, str]:
    card = cards['CardShapedThings'][card_name]
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

class DominionCardsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parsing_table = False
        self.parsing_th = False
        self.parsing_td = False
        self.is_header_row = True
        self.column_index = 0
        self.headers: list[str] = []
        self.current_card = create_card()
        self.piles: dict[str, dict[str, Any]] = {}
        self.cards: dict[str, Any] = {
            'CardShapedThings': {},
            'Base': [],
            'KingdomPiles': [],
            'NonSupply': [],
            'Shelters': [],
            'Ruins': [],
            'Events': [],
            'Landmarks': [],
            'Heirlooms': [],
            'Zombies': [],
            'Boons': [],
            'Hexes': [],
            'States': [],
            'Projects': [],
            'Artifacts': [],
            'Ways': [],
            'Allies': [],
            'Traits': [],
            'Prophecies': [],
        }

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == 'table':
            self.parsing_table = True
        elif tag == 'th':
            self.parsing_th = True
        elif tag == 'td':
            self.parsing_td = True
        elif tag == 'img':
            column_name = self.headers[self.column_index]
            if column_name == 'Name':
                for name, value in attrs:
                    if name == 'src' and value is not None:
                        self.current_card['Image'] = value
            elif column_name == 'Cost':
                for name, value in attrs:
                    if name == 'alt' and value is not None:
                        if self.current_card['Cost'] != '':
                            self.current_card['Cost'] += ' '
                        self.current_card['Cost'] += value
            elif column_name == 'Text':
                for name, value in attrs:
                    if name == 'alt' and value is not None:
                        self.current_card['Text'] += value
        elif tag == 'a':
            if self.parsing_table:
                column_name = self.headers[self.column_index]
                if column_name == 'Name':
                    for name, value in attrs:
                        if name == 'href' and value is not None:
                            self.current_card['Link'] = value

    def handle_endtag(self, tag: str) -> None:
        if tag == 'table':
            self.parsing_table = False
        elif tag == 'tr':
            self.column_index = 0
            if self.is_header_row:
                self.is_header_row = False
            else:
                set_name: str = self.current_card['Set']['Name']
                if ',' in set_name:
                    split = set_name.split(',')
                    self.current_card['Set']['Name'] = split[0].strip()
                    edition = split[1].strip()
                    self.current_card['Set']['Edition'] = edition
                    assert edition in {'1E', '2E'}, f'{edition} is not a valid edition'
                else:
                    self.current_card['Set']['Name'] = set_name.strip()

                card_name = self.current_card['Name']
                self.cards['CardShapedThings'][card_name] = self.current_card

                if is_base_card(self.current_card):
                    self.cards['Base'].append(card_name)
                elif is_non_supply_card(self.current_card):
                    self.cards['NonSupply'].append(card_name)
                elif 'Shelter' in self.current_card['Types']:
                    self.cards['Shelters'].append(card_name)
                elif 'Ruins' in self.current_card['Types']:
                    self.cards['Ruins'].append(card_name)
                elif self.current_card['Types'][0] == 'Event':
                    self.cards['Events'].append(card_name)
                elif self.current_card['Types'][0] == 'Landmark':
                    self.cards['Landmarks'].append(card_name)
                elif 'Heirloom' in self.current_card['Types']:
                    self.cards['Heirlooms'].append(card_name)
                elif 'Zombie' in self.current_card['Types']:
                    self.cards['Zombies'].append(card_name)
                elif self.current_card['Types'][0] == 'Boon':
                    self.cards['Boons'].append(card_name)
                elif self.current_card['Types'][0] == 'Hex':
                    self.cards['Hexes'].append(card_name)
                elif self.current_card['Types'][0] == 'State':
                    self.cards['States'].append(card_name)
                elif self.current_card['Types'][0] == 'Project':
                    self.cards['Projects'].append(card_name)
                elif self.current_card['Types'][0] == 'Artifact':
                    self.cards['Artifacts'].append(card_name)
                elif self.current_card['Types'][0] == 'Way':
                    self.cards['Ways'].append(card_name)
                elif self.current_card['Types'][0] == 'Ally':
                    self.cards['Allies'].append(card_name)
                elif self.current_card['Types'][0] == 'Trait':
                    self.cards['Traits'].append(card_name)
                elif self.current_card['Types'][0] == 'Prophecy':
                    self.cards['Prophecies'].append(card_name)
                else:
                    assert_kingdom_card_types(self.current_card['Types'])
                    pile_name = get_pile_name(self.current_card)
                    pile = self.piles.get(pile_name)
                    if pile is None:
                        pile = {
                            'Name': pile_name,
                            'Cards': [],
                        }
                        self.piles[pile_name] = pile
                        self.cards['KingdomPiles'].append(pile)

                    pile['Cards'].append(card_name)
                    pile['Cards'].sort(key=lambda card_name: card_comparison_key(card_name, self.cards))

                self.current_card = create_card()
        elif tag == 'th':
            self.parsing_th = False
            self.column_index += 1
        elif tag == 'td':
            self.parsing_td = False
            self.column_index += 1

    def handle_data(self, data: str) -> None:
        if self.parsing_td:
            column_name = self.headers[self.column_index]
            match column_name:
                case 'Name':
                    self.current_card['Name'] = data.strip()
                case 'Set':
                    self.current_card['Set']['Name'] += data
                case 'Types':
                    self.current_card['Types'] = [t.strip() for t in data.split('-')]
                case 'Text':
                    column_name = self.headers[self.column_index]
                    if column_name == 'Text':
                        self.current_card['Text'] += data.replace('\u00a0', ' ').replace('\u200a', '').replace('\u2013', '-').replace('\u2019', "'")
        elif self.parsing_th:
            self.headers.append(data.strip())

def to_python_const(name: str) -> str:
    const_name = ''
    last_is_lower = False
    for char in name:
        if char == "'":
            pass
        elif char in {' ', '-'}:
            const_name += '_'
        else:
            if char.isupper() and last_is_lower:
                const_name += '_'
            const_name += char.upper()

        last_is_lower = char.islower()

    return const_name

def gen_python_card_shaped_things_consts(io: IO[str], cards: dict[str, Any]) -> None:
    for card_shaped_thing in cards['CardShapedThings'].values():
        name = card_shaped_thing['Name']
        const_name = to_python_const(name)
        types = '{' + ', '.join(f'"{t}"' for t in card_shaped_thing['Types']) + '}'
        cost_str = card_shaped_thing['Cost']
        cost_split = cost_str.split()
        cost_init_parts: list[str] = []
        for part in cost_split:
            if part[0] == '$':
                s = part[1:]
                if s[-1] in {'*', '+'}:
                    s = s[:-1]
                cost_init_parts.append(f'coins={s}')
            elif part[-1] == 'P':
                cost_init_parts.append('potions=' + ('1' if len(part) == 1 else part[:-1]))
            elif part[-1] == 'D':
                cost_init_parts.append('debt=' + ('1' if len(part) == 1 else part[:-1]))
            else:
                assert False, f'Unknown cost part: {part}'
        cost_init_str = ', '.join(cost_init_parts)
        s = card_shaped_thing['Set']
        set_name = '"' + s['Name'] + '"'
        set_edition = s['Edition']
        if set_edition is None:
            set_init_str = f'Set({set_name})'
        else:
            set_init_str = f'Set({set_name}, "{set_edition}")'
        text = card_shaped_thing['Text'].replace('"', '\\"')
        link = card_shaped_thing['Link']
        image = card_shaped_thing['Image']

        io.write(f'{const_name} = CardShapedThing("{name}", {types}, Cost({cost_init_str}), {set_init_str}, "{text}", "{link}", "{image}")\n')

def gen_python_card_shaped_things_dict(io: IO[str], cards: dict[str, Any]) -> None:
    io.write('\nCARD_SHAPED_THINGS = {\n')

    for card_shaped_thing in cards['CardShapedThings'].values():
        name = card_shaped_thing['Name']
        const_name = to_python_const(name)
        io.write(f'    "{name}": {const_name},\n')

    io.write('}\n')

def gen_python_list(io: IO[str], cards: dict[str, Any], list_name: str) -> None:
    list_name_const = to_python_const(list_name)
    io.write(f'\n{list_name_const} = [\n')

    for name in cards[list_name]:
        const_name = to_python_const(name)
        io.write(f'    {const_name},\n')

    io.write(']\n')

def gen_python_kingdom_piles(io: IO[str], kingdom_piles: list[dict[str, Any]]) -> None:
    io.write(f'\nKINGDOM_PILES = [\n')

    for pile in kingdom_piles:
        cards_list = ', '.join(to_python_const(c) for c in pile['Cards'])
        if len(pile['Cards']) == 1:
            io.write(f'    Pile([{cards_list}]),\n')
        else:
            io.write(f'    Pile([{cards_list}], "{pile["Name"]}"),\n')

    io.write(']\n')

def gen_python(cards: dict[str, Any]) -> None:
    path = Path('dominion') / 'card_shaped_things.py'
    with path.open('w', encoding='utf8') as f:
        f.write('from .base import CardShapedThing, Cost, Pile, Set\n\n')

        gen_python_card_shaped_things_consts(f, cards)
        gen_python_card_shaped_things_dict(f, cards)
        for list_name in [
            'Base',
            'NonSupply',
            'Shelters',
            'Ruins',
            'Events',
            'Landmarks',
            'Heirlooms',
            'Zombies',
            'Boons',
            'Hexes',
            'States',
            'Projects',
            'Artifacts',
            'Ways',
            'Allies',
            'Traits',
            'Prophecies',
        ]:
            gen_python_list(f, cards, list_name)

        gen_python_kingdom_piles(f, cards['KingdomPiles'])

def main() -> None:
    cards_list_filename = 'list_of_cards.html'

    with open(cards_list_filename, 'r', encoding='utf8') as f:
        html_text = f.read()

    parser = DominionCardsParser()
    parser.feed(html_text)

    with open('dominion_cards.json', 'w', encoding='utf8') as f:
        json.dump(parser.cards, f, indent=2)

    gen_python(parser.cards)

if __name__ == '__main__':
    main()
