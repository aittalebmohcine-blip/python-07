from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


# EliteCard (Multiple Inheritance: Card + Combatable + Magical)
class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        damage_blocked: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(damage, int) or damage <= 0:
            raise Exception(
                "[INITIALIZATION ERROR]: The damage argument must be a positive non zero integer"
            )
        if not isinstance(damage_blocked, int) or damage < 0:
            raise Exception(
                "[INITIALIZATION ERROR]: The damage_blocked argument must be a positive integer"
            )
        if not isinstance(health, int) or health <= 0:
            raise Exception(
                "[INITIALIZATION ERROR]: The health argument must be a positive non zero integer"
            )
        self.damage = damage
        self.health = health
        self.damage_blocked = damage_blocked
        self.type = "Elite"

    # from Card
    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError("[LOGIC ERROR]: The game_state argument must be a dict.")
        if "mana" not in game_state:
            raise ValueError(
                "[LOGIC ERROR]: missing 'mana' key in game_state argument!"
            )
        if "battlefield" not in game_state:
            raise ValueError(
                "[LOGIC ERROR]: missing 'battlefield' key in game_state argument!"
            )
        if not self.is_playable(game_state["mana"]):
            raise ValueError(
                "[LOGIC ERROR]: The available 'mana' is not enough to play this card."
            )
        game_state["battlefield"][self.name] = self.get_card_info()
        game_state["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.name} summoned to battlefield",
        }

    # from Combatable
    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            raise TypeError("[LOGIC ERROR]: The target argument is not a Card instance")
        if not hasattr(target, "health"):
            raise AttributeError(
                "[LOGIC ERROR]: The target can't be attacked, it has no health attribute"
            )
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage <= 0:
            raise Exception(
                "[LOGIC ERROR]: The incoming_damage argument must be a positive non zero integer"
            )
        if incoming_damage - self.damage_blocked > 0:
            self.health -= incoming_damage - self.damage_blocked
        if self.health < 0:
            self.health = 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.damage_blocked,
            "still_alive": True if self.health > 0 else False,
        }

    def get_combat_stats(self) -> dict:
        pass

    # from Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(spell_name, str):
            raise TypeError(
                "[LOGIC ERROR]: The spell_name argument must be a string type."
            )

        if not isinstance(targets, list):
            raise TypeError("[LOGIC ERROR]: The targets argument must be a list.")

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount <= 0:
            raise Exception(
                "[LOGIC ERROR]: The amount argument must be a positive non zero integer"
            )
        return {"channeled": amount, "total_mana": 7}

    def get_magic_stats(self) -> dict:
        pass
