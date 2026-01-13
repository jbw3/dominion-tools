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
