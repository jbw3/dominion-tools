from collections import namedtuple
from typing import NamedTuple

class Cost:
    Values = namedtuple('Values', ['coins', 'potions', 'debt'])

    def __init__(self, coins: int=0, potions: int=0, debt: int=0):
        self._values = Cost.Values(coins, potions, debt)

    @property
    def coins(self) -> int:
        return self._values.coins

    @property
    def potions(self) -> int:
        return self._values.potions

    @property
    def debt(self) -> int:
        return self._values.debt

    def __repr__(self) -> str:
        return f'Cost({self.coins}, {self.potions}, {self.debt})'

    def __str__(self) -> str:
        parts: list[str] = []
        if self.coins > 0:
            parts.append(f'${self.coins}')
        if self.potions > 0:
            parts.append('P')
        if self.debt > 0:
            parts.append(f'{self.debt}D')

        return ' '.join(parts)

    def __hash__(self) -> int:
        return hash(self._values)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values == Cost(value)._values
        elif isinstance(value, Cost):
            return self._values == value._values
        raise TypeError(f"'==' not supported between instances of 'Cost' and '{type(value)}'")

    def __ne__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values != Cost(value)._values
        elif isinstance(value, Cost):
            return self._values != value._values
        raise TypeError(f"'!=' not supported between instances of 'Cost' and '{type(value)}'")

    def __lt__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values < Cost(value)._values
        elif isinstance(value, Cost):
            return self._values < value._values
        raise TypeError(f"'<' not supported between instances of 'Cost' and '{type(value)}'")

    def __le__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values <= Cost(value)._values
        elif isinstance(value, Cost):
            return self._values <= value._values
        raise TypeError(f"'<=' not supported between instances of 'Cost' and '{type(value)}'")

    def __gt__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values > Cost(value)._values
        elif isinstance(value, Cost):
            return self._values > value._values
        raise TypeError(f"'>' not supported between instances of 'Cost' and '{type(value)}'")

    def __ge__(self, value: object) -> bool:
        if isinstance(value, int):
            return self._values >= Cost(value)._values
        elif isinstance(value, Cost):
            return self._values >= value._values
        raise TypeError(f"'>=' not supported between instances of 'Cost' and '{type(value)}'")

class Set(NamedTuple):
    name: str
    edition: str|None = None

class CardShapedThing:
    def __init__(self, name: str, types: set[str], cost: Cost, set: Set, text: str, link: str, image: str):
        self.name = name
        self.types = types
        self.cost = cost
        self.set = set
        self.text = text
        self.link = link
        self.image = image

class Pile:
    def __init__(self, cards: list[CardShapedThing], name: str|None=None):
        self.cards = cards
        if name is not None:
            self.name = name
        else:
            self.name = '/'.join(c.name for c in self.cards)
