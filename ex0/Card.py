from abc import ABC, abstractmethod
# from typing import Any


# Card (Abstract Base Class)
class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str):
            raise TypeError("The name should be a string type.\n")
        self.name = name

        if not isinstance(cost, int) or cost <= 0:
            raise Exception("Cost must be a positive non zero integer\n")
        self.cost = cost

        if not isinstance(rarity, str):
            raise TypeError("Rarity should be a string type.\n")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return vars(self)

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError("available_mana must be a non-negative integer\n")
        return available_mana >= self.cost
