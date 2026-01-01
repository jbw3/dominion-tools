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
    if card['Name'] in {'Horse'}:
        return True

    for t in card['Types']:
        if t in {'Loot', 'Prize', 'Reward', 'Spirit', 'Zombie'}:
            return True

    return False

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
        self.cards: dict[str, Any] = {
            'CardShapedThings': {},
            'Base': [],
            'Kingdom': [],
            'NonSupply': [],
            'Shelters': [],
            'Ruins': [],
            'Events': [],
            'Landmarks': [],
            'Heirlooms': [],
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
                    self.cards['Kingdom'].append(card_name)

                self.cards['CardShapedThings'][card_name] = self.current_card

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
