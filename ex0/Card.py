from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: "
                "The name argument should be a string type."
            )
        self.name = name

        if not isinstance(cost, int) or cost <= 0:
            raise Exception(
                "[INITIALIZATION ERROR]: "
                "The cost argument must be a positive non zero integer"
            )
        self.cost = cost

        if not isinstance(rarity, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: "
                "The rarity should be a string type."
            )
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass

    play = abstractmethod(play)

    def get_card_info(self) -> dict:
        return vars(self)

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int) or available_mana < 0:
            raise ValueError(
                "[LOGIC ERROR]: "
                "The available_mana must be a non-negative integer"
            )
        return available_mana >= self.cost
