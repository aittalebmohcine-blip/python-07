from ex3.GameStrategy import GameStrategy
from operator import attrgetter


class AggressiveStrategy(GameStrategy):
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError(
                "[INITIALIZATION ERROR]: "
                "The name argument should be a string type."
            )
        self.name = name

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if not isinstance(hand, list) or not isinstance(battlefield, list):
            raise TypeError(
                "[LOGIC ERROR]: The hand and "
                "battlefield arguments must be lists."
            )

        cards_played = []
        mana_used = 0

        for card in hand:
            if hasattr(card, "cost"):
                battlefield.append(card)
                cards_played.append(card)
                mana_used += card.cost

        damage_dealt = 0
        for card in battlefield:
            if getattr(card, "type", "") == "Creature":
                if hasattr(card, "attack"):
                    damage_dealt += card.attack

        return {
            "cards_played": [card.name for card in cards_played],
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: list) -> list:
        if not isinstance(available_targets, list):
            raise TypeError(
                "[LOGIC ERROR]: The available_targets argument must be a list."
            )

        with_health = [
            target for target in available_targets if hasattr(target, "health")
        ]
        without_health = [
            target for target in available_targets
            if not hasattr(target, "health")
            ]

        sorted_targets = sorted(
            with_health, key=attrgetter("health")
            ) + without_health

        high_prior_targets = [
            target
            for target in sorted_targets
            if getattr(target, "name", "") == "Enemy Player"
        ]
        sorted_targets = [
            target for target in sorted_targets if
            target not in high_prior_targets
        ]

        final_list = high_prior_targets + sorted_targets
        return final_list
