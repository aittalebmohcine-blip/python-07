from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand = []
        self.battlefield = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        if not isinstance(factory, CardFactory):
            raise TypeError(
                "[LOGIC ERROR]: The factory argument "
                "must be a CardFactory instance"
            )
        if not isinstance(strategy, GameStrategy):
            raise TypeError(
                "[LOGIC ERROR]: The strategy argument "
                "must be a GameStrategy instance"
            )
        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand = []
        self.battlefield = []

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise ValueError(
                "[LOGIC ERROR]: Can't simulate turn. "
                "Game engine is not configured (missing factory or strategy)."
            )
        self.hand = [
            self.factory.create_creature(),
            self.factory.create_spell(),
            self.factory.create_artifact(),
        ]
        self.cards_created += 3
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy
            else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
