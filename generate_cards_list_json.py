from html.parser import HTMLParser
import json
from typing import Any

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
            if column_name == 'Cost':
                for name, value in attrs:
                    if name == 'alt' and value is not None:
                        if self.current_card['Cost'] != '':
                            self.current_card['Cost'] += ' '
                        self.current_card['Cost'] += value
            elif column_name == 'Text':
                for name, value in attrs:
                    if name == 'alt' and value is not None:
                        self.current_card['Text'] += value

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

def main() -> None:
    cards_list_filename = 'list_of_cards.html'

    with open(cards_list_filename, 'r', encoding='utf8') as f:
        html_text = f.read()

    parser = DominionCardsParser()
    parser.feed(html_text)

    with open('dominion_cards.json', 'w', encoding='utf8') as f:
        json.dump(parser.cards, f, indent=2)

if __name__ == '__main__':
    main()
