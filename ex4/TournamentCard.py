from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError(
                "[INITIALIZATION ERROR]: Attack and health must be positive"
            )

        self.attack = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    # Card
    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state["mana"]):
            raise ValueError("Not enough mana")

        game_state["mana"] -= self.cost
        game_state["battlefield"].append(self)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    # Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage

        if self.health < 0:
            self.health = 0

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack,
            "health": self.health,
        }

    # Rankable
    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    #####
    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack,
            "health": self.health,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }
