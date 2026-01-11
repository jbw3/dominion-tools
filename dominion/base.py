class Cost:
    def __init__(self, coins: int=0, potions: int=0, debt: int=0):
        self._coins = coins
        self._potions = potions
        self._debt = debt

    @property
    def coins(self) -> int:
        return self._coins

    @property
    def potions(self) -> int:
        return self._potions

    @property
    def debt(self) -> int:
        return self._debt

class CardShapedThing:
    def __init__(self, name: str, cost: Cost, text: str, link: str):
        self.name = name
        self.cost = cost
        self.text = text
        self.link = link
