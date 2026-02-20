from ex3.GameStrategy import GameStrategy
from operator import attrgetter


# AggressiveStrategy (Concrete Strategy)
class AggressiveStrategy(GameStrategy):
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: The name argument should be a string type."
            )
        self.name = name

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        if not isinstance(available_targets, list):
            raise TypeError(
                "LOGIC ERROR: The available_targets argument must be a list"
            )

        with_health = [
            target for target in available_targets if hasattr(target, "health")
        ]
        without_health = [
            target for target in available_targets if not hasattr(target, "health")
        ]

        sorted_targets = sorted(with_health, key=attrgetter("health")) + without_health

        for target in sorted_targets:
            high_preior_targets = []
            if hasattr(target, "name") and getattr(target, "name") == "Enemy Player":
                high_preior_targets.append(target)
        sorted_targets = [
            target for target in sorted_targets if target not in high_preior_targets
        ]
        final_list = high_preior_targets + sorted_targets

        return final_list
