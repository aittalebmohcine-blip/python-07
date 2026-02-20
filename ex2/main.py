from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def main() -> None:

    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    parents = EliteCard.__bases__
    for parent in parents:
        methods = [
            m
            for m in dir(parent)
            if callable(getattr(parent, m)) and not m.startswith("__")
        ]
        print(f"- {parent.__name__}: {methods}")

    try:
        warrior = EliteCard("Arcane Warrior", 2, "rar", 5, 3, 1)
    except Exception as e:
        warrior = None
        print(e)
    try:
        enemy = CreatureCard("Enemy", 9, "rar", 2, 1)
    except Exception as e:
        enemy = None
        print(e)

    if warrior:
        print(f"\nPlaying {warrior.name} ({warrior.type} Card):")
        try:
            if enemy:
                print("\nCombat phase:")
                print(f"Attack result: {warrior.attack(enemy)}")
                print(f"Defense result: {warrior.defend(enemy.attack)}")

            print("\nMagic phase:")
            print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
            print(f"Mana channel: {warrior.channel_mana(3)}")
        except Exception as e:
            print(e)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
