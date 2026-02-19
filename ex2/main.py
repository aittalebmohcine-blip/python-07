#   === DataDeck Ability System ===
#
#   EliteCard capabilities:
#   - Card: ['play', 'get_card_info', 'is_playable']
#   - Combatable: ['attack', 'defend', 'get_combat_stats']
#   - Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']
#
#   Playing Arcane Warrior (Elite Card):
#
#   Combat phase:
#   Attack result: {'attacker': 'Arcane Warrior', 'target': 'Enemy', 'damage': 5, 'combat_type': 'melee'}
#   Defense result: {'defender': 'Arcane Warrior', 'damage_taken': 2, 'damage_blocked': 3, 'still_alive': True}
#
#   Magic phase:
#   Spell cast: {'caster': 'Arcane Warrior', 'spell': 'Fireball', 'targets': ['Enemy1', 'Enemy2'], 'mana_used': 4}
#   Mana channel: {'channeled': 3, 'total_mana': 7}
#
#   Multiple interface implementation successful!


from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard
# from ex1.SpellCard import SpellCard


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

    if warrior and enemy:
        print(f"\nPlaying {warrior.name} ({warrior.type} Card):")
        try:
            print(f"\nAttack result: {warrior.attack(enemy)}")
            print(f"Defense result: {warrior.defend(enemy.attack)}")
        except Exception as e:
            print(e)

    print("\nMagic phase:")
    print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
