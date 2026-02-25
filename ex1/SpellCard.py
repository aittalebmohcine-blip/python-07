from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: "
                "The effect_type argument must be a string type."
            )
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError(
                "[LOGIC ERROR]: The game_state argument must be a "
                "Dictionary type."
            )

        if "mana" not in game_state:
            raise KeyError(
                "[LOGIC ERROR]: missing 'mana' key in game_state!"
            )

        if not self.is_playable(game_state["mana"]):
            raise ValueError(
                "[LOGIC ERROR]: The available mana is not enough "
                "to play this card."
            )

        game_state.update({"mana": game_state["mana"] - self.cost})

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (
                f"Deal {self.cost} "
                f"{self.effect_type} to target"
            ),
        }

    def resolve_effect(self, targets: list) -> dict:
        if not isinstance(targets, list):
            raise TypeError(
                "[LOGIC ERROR]: The targets argument must be a list "
                "of instances of the CreatureCard class"
            )

        for target in targets:
            if not isinstance(target, CreatureCard):
                raise TypeError(
                    "[LOGIC ERROR]: The targets argument must be a "
                    "list of instances of the CreatureCard class"
                )

        if self.effect_type == "damage":
            for target in targets:
                target.health -= self.cost
        elif self.effect_type == "heal":
            for target in targets:
                target.health += self.cost
        elif self.effect_type == "buff":
            for target in targets:
                target.health += 1
                target.attack += 1

        return {
            "card_played": self.name,
            "effect_type": self.effect_type,
            "targets_effected": [
                target.name for target in targets
            ],
        }
