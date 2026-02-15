from ex0.Card import Card


# CreatureCard (Concrete Implementation)
class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive intiger\n")
        self.attack = attack
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive non zero intiger\n")
        self.health = health

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError("Game state must be a dict.\n")
        if "mana" not in game_state:
            raise ValueError("missing mana key in game_state!\n")
        if "battlefield" not in game_state:
            raise ValueError("missing battlefield key in game_state!\n")
        if not self.is_playable(game_state["mana"]):
            raise ValueError("The available mana is not enough to play this card.\n")
        game_state["battlefield"][self.name] = self.get_card_info()
        game_state.update({"mana": (game_state["mana"] - self.cost)})
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        if not isinstance(target, CreatureCard):
            raise TypeError("The target should be an isinstance of the CreatureCard.\n")
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
