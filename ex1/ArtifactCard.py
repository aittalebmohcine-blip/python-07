from ex0.Card import Card


# ArtifactCard (Concrete Implementation)
class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:

        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError(
                "[INITIALIZATION ERROR]: The durability argument must be a positive non-zero  integer."
            )
        self.durability = durability

        if not isinstance(effect, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: The effect argument must be a string type."
            )
        self.effect = effect

        self.type = "Artifact"

    #   Play result: {'card_played': 'Mana Crystal', 'mana_used': 2, 'effect': 'Permanent: +1 mana per turn'}
    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError(
                "[LOGIC ERROR]: The game_state argument must be a Dictionary type."
            )
        if "mana" not in game_state:
            raise KeyError("[LOGIC ERROR]: missing 'mana' key in game_state argument!")
        if not self.is_playable(game_state["mana"]):
            raise ValueError(
                "[LOGIC ERROR]: The available mana is not enough to play this card."
            )
        game_state["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> dict:
        return {
            "ability_activated": self.name,
            "effect": self.effect,
            "durability": self.durability,
        }
