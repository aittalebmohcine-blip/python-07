from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = [
            {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": "Legendary",
                "attack": 7,
                "health": 5,
            },
            {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 1,
            },
            {
                "name": "Ice Wizard",
                "cost": 4,
                "rarity": "Rare",
                "attack": 3,
                "health": 4,
            },
            {
                "name": "Lightning Elemental",
                "cost": 3,
                "rarity": "Uncommon",
                "attack": 4,
                "health": 2,
            },
            {
                "name": "Stone Golem",
                "cost": 6,
                "rarity": "Rare",
                "attack": 5,
                "health": 8,
            },
            {
                "name": "Shadow Assassin",
                "cost": 3,
                "rarity": "Uncommon",
                "attack": 5,
                "health": 2,
            },
            {
                "name": "Healing Angel",
                "cost": 4,
                "rarity": "Rare",
                "attack": 2,
                "health": 6,
            },
            {
                "name": "Forest Sprite",
                "cost": 1,
                "rarity": "Common",
                "attack": 1,
                "health": 1,
            },
        ]

        self._spells = [
            {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": "Common",
                "effect_type": "damage",
            },
            {
                "name": "Healing Potion",
                "cost": 2,
                "rarity": "Common",
                "effect_type": "heal",
            },
            {
                "name": "Fireball",
                "cost": 4,
                "rarity": "Uncommon",
                "effect_type": "damage",
            },
            {
                "name": "Shield Spell",
                "cost": 1,
                "rarity": "Common",
                "effect_type": "buff",
            },
            {
                "name": "Meteor",
                "cost": 8,
                "rarity": "Legendary",
                "effect_type": "damage",
            },
            {
                "name": "Ice Shard",
                "cost": 2,
                "rarity": "Common",
                "effect_type": "damage",
            },
            {
                "name": "Divine Light",
                "cost": 5,
                "rarity": "Rare",
                "effect_type": "heal",
            },
            {
                "name": "Magic Missile",
                "cost": 1,
                "rarity": "Common",
                "effect_type": "damage",
            },
        ]

        self._artifacts = [
            {
                "name": "Mana Crystal",
                "cost": 2,
                "rarity": "Common",
                "durability": 5,
                "effect": "Permanent: +1 mana per turn",
            },
            {
                "name": "Sword of Power",
                "cost": 3,
                "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: +2 attack to equipped creature",
            },
            {
                "name": "Ring of Wisdom",
                "cost": 4,
                "rarity": "Rare",
                "durability": 4,
                "effect": "Permanent: Draw an extra card each turn",
            },
            {
                "name": "Shield of Defense",
                "cost": 5,
                "rarity": "Rare",
                "durability": 6,
                "effect": "Permanent: +3 health to all friendly creatures",
            },
            {
                "name": "Crown of Kings",
                "cost": 7,
                "rarity": "Legendary",
                "durability": 8,
                "effect": "Permanent: +1 cost reduction to all cards",
            },
            {
                "name": "Boots of Speed",
                "cost": 2,
                "rarity": "Uncommon",
                "durability": 2,
                "effect": "Permanent: Cards cost 1 less mana",
            },
            {
                "name": "Cloak of Shadows",
                "cost": 3,
                "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: Creatures have stealth",
            },
            {
                "name": "Staff of Elements",
                "cost": 6,
                "rarity": "Legendary",
                "durability": 7,
                "effect": "Permanent: +1 spell damage",
            },
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for creature in self._creatures:
                if creature["name"].lower() == name_or_power.lower():
                    return CreatureCard(
                        creature["name"],
                        creature["cost"],
                        creature["rarity"],
                        creature["attack"],
                        creature["health"],
                    )
        if isinstance(name_or_power, int):
            return CreatureCard("Custom Creature", 2, "Common",
                                name_or_power, 1)
        creature = self._creatures[0]
        return CreatureCard(
            creature["name"],
            creature["cost"],
            creature["rarity"],
            creature["attack"], creature["health"]
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for spell in self._spells:
                if spell["name"].lower() == name_or_power.lower():
                    return SpellCard(
                        spell["name"],
                        spell["cost"],
                        spell["rarity"],
                        spell["effect_type"],
                    )
        if isinstance(name_or_power, int):
            return SpellCard("Custom Spell", name_or_power, "Common", "damage")
        spell = self._spells[0]
        return SpellCard(spell["name"], spell["cost"], spell["rarity"],
                         spell["effect_type"])

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            for artifact in self._artifacts:
                if artifact["name"].lower() == name_or_power.lower():
                    return ArtifactCard(
                        artifact["name"],
                        artifact["cost"],
                        artifact["rarity"],
                        artifact["durability"],
                        artifact["effect"],
                    )
        if isinstance(name_or_power, int):
            return ArtifactCard(
                "Custom Artifact",
                name_or_power,
                "Common",
                3,
                "Permanent: Custom effect",
            )
        artifact = self._artifacts[0]
        return ArtifactCard(
            artifact["name"],
            artifact["cost"],
            artifact["rarity"],
            artifact["durability"], artifact["effect"]
            )

    def create_themed_deck(self, size: int) -> dict:
        if not isinstance(size, int) or size <= 0:
            raise Exception(
                "[LOGIC ERROR]: The size argument must "
                "be a positive non-zero integer"
            )
        deck = {"creatures": [], "spells": [], "artifacts": []}
        for _ in range(size):
            card_type = random.choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                deck["creatures"].append(self.create_creature())
            elif card_type == "spell":
                deck["spells"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())
        deck["size"] = size
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": [element["name"] for element in self._creatures],
            "spells": [element["name"] for element in self._spells],
            "artifacts": [element["name"] for element in self._artifacts],
        }
