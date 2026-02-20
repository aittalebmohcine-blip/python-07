#   === DataDeck Game Engine ===
#
#   Configuring Fantasy Card Game...
#   Factory: FantasyCardFactory
#   Strategy: AggressiveStrategy
#   Available types: {'creatures': ['dragon', 'goblin'], 'spells': ['fireball'], 'artifacts': ['mana_ring']}
#
#   Simulating aggressive turn...
#   Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]
#
#   Turn execution:
#   Strategy: AggressiveStrategy
#   Actions: {'cards_played': ['Goblin Warrior', 'Lightning Bolt'], 'mana_used': 5, 'targets_attacked': ['Enemy Player'], 'damage_dealt': 8}
#
#   Game Report:
#   {'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy', 'total_damage': 8, 'cards_created': 3}
#
#   Abstract Factory + Strategy Pattern: Maximum flexibility achieved!

from ex3.AggressiveStrategy import AggressiveStrategy

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    print("Factory: ")
    aggressive_startegy = AggressiveStrategy("AggressiveStrategy")
    p1 = CreatureCard("Enemy Player", 1, "r", 1, 1)
    p2 = CreatureCard("p2", 2, "r", 2, 2)
    p3 = CreatureCard("p3", 3, "r", 3, 3)
    llll = aggressive_startegy.prioritize_targets([p3, p2, p1])
    print(
        [ll.name for ll in llll if hasattr(ll, "health")]
        + [ll for ll in llll if not hasattr(ll, "health")]
    )


if __name__ == "__main__":
    main()
