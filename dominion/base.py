from typing import NamedTuple

class Cost(NamedTuple):
    coins: int = 0
    potions: int = 0
    debt: int = 0

class CardShapedThing:
    def __init__(self, name: str, types: set[str], cost: Cost, text: str, link: str):
        self.name = name
        self.types = types
        self.cost = cost
        self.text = text
        self.link = link

class Pile:
    def __init__(self, cards: list[CardShapedThing], name: str|None=None):
        self.cards = cards
        if name is not None:
            self.name = name
        else:
            self.name = '/'.join(c.name for c in self.cards)
