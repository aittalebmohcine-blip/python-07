from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


# EliteCard (Multiple Inheritance: Card + Combatable + Magical)
class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, damage: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(damage, int) or damage <= 0:
            raise Exception(
                "[INITIALIZATION ERROR]: The damage argument must be a positive non zero integer"
            )
        self.damage = damage

    # from Card
    def play(self, game_state: dict) -> dict:
        pass

    # from Combatable
    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            raise TypeError("[LOGIC ERROR]: The target argument is not a Card instance")
        try:
            attr_target_health = getattr(target, "health")
        except AttributeError:
            raise AttributeError(
                "[ATTRIBUTE ERROR]: The target can't be attacked, it has no health attribute"
            )
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    # from Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass
