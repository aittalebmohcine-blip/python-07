from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    game_state = {"mana": 60, "battlefield": {}}

    print("Building deck with different card types...")
    deck = Deck()
    data = {
        "creature_cards": [
            ("Fire Dragon", 5, "Legendary", 7, 5),
        ],
        "artifact_cards": [
            (
                "Mana Crystal",
                2,
                "Common",
                5,
                "Permanent: +1 mana per turn",
            ),
        ],
        "spell_cards": [
            ("Lightning Bolt", 3, "Common", "damage"),
        ],
    }

    for key in data:
        if key == "creature_cards":
            try:
                for card_data in data[key]:
                    try:
                        name, cost, rarity, attack, health = card_data
                        card = CreatureCard(
                            name,
                            cost,
                            rarity,
                            attack,
                            health,
                        )
                        deck.add_card(card)
                    except Exception as e:
                        print(e)
            except TypeError as e:
                print(e)

        if key == "artifact_cards":
            try:
                for card_data in data[key]:
                    try:
                        (
                            name,
                            cost,
                            rarity,
                            durability,
                            effect,
                        ) = card_data
                        card = ArtifactCard(
                            name,
                            cost,
                            rarity,
                            durability,
                            effect,
                        )
                        deck.add_card(card)
                    except Exception as e:
                        print(e)
            except TypeError as e:
                print(e)

        if key == "spell_cards":
            try:
                for card_data in data[key]:
                    try:
                        name, cost, rarity, effect_type = card_data
                        card = SpellCard(
                            name,
                            cost,
                            rarity,
                            effect_type,
                        )
                        deck.add_card(card)
                    except Exception as e:
                        print(e)
            except TypeError as e:
                print(e)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    count = stats["total_cards"]
    for _ in range(count):
        try:
            drew = deck.draw_card()
            print(f"\nDrew: {drew.name} ({drew.type})")
            print(f"Play result: {drew.play(game_state)}")
        except Exception as e:
            print(e)

    print(
        "\nPolymorphism in action: "
        "Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
