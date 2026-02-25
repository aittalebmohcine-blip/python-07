from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError(
                "[INITIALIZATION ERROR]: "
                "The attack argument must be a positive intiger"
            )
        self.attack = attack

        if not isinstance(health, int) or health <= 0:
            raise ValueError(
                "[INITIALIZATION ERROR]: "
                "The health argument must be a positive non zero intiger"
            )
        self.health = health

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError(
                "[LOGIC ERROR]: The game_state argument must be a dict."
            )

        if "mana" not in game_state:
            raise ValueError(
                "[LOGIC ERROR]: missing 'mana' key in game_state argument!"
            )

        if "battlefield" not in game_state:
            raise ValueError(
                "[LOGIC ERROR]: missing 'battlefield' key in game_state "
                "argument!"
            )

        if not self.is_playable(game_state["mana"]):
            raise ValueError(
                "[LOGIC ERROR]: The available 'mana' is not enough "
                "to play this card."
            )

        game_state["battlefield"][self.name] = self.get_card_info()
        game_state.update({"mana": game_state["mana"] - self.cost})

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        if not isinstance(target, CreatureCard):
            raise TypeError(
                "[LOGIC ERROR]: The target argument should be an "
                "isinstance of the CreatureCard."
            )

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
