from html.parser import HTMLParser
import json
from typing import Any

class DominionCardsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parsing_table = False
        self.parsing_th = False
        self.parsing_td = False
        self.is_header_row = True
        self.column_index = 0
        self.headers: list[str] = []
        self.current_card = {}
        self.cards: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == 'table':
            self.parsing_table = True
        elif tag == 'th':
            self.parsing_th = True
        elif tag == 'td':
            self.parsing_td = True

    def handle_endtag(self, tag: str) -> None:
        if tag == 'table':
            self.parsing_table = False
        elif tag == 'tr':
            self.column_index = 0
            if self.is_header_row:
                self.is_header_row = False
            else:
                self.cards.append(self.current_card)
                self.current_card = {}
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
                case 'Types':
                    self.current_card['Types'] = [t.strip() for t in data.split('-')]
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
