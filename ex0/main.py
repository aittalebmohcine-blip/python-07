from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    try:
        card_1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    except Exception as e:
        print(e)
        card_1 = None

    try:
        card_2 = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    except Exception as e:
        print(e)
        card_2 = None

    game_state = {"mana": 6, "battlefield": {}}

    if card_1:
        print("Testing Abstract Base Class Design:\n")

        print("CreatureCard Info:")
        print(card_1.get_card_info())

        try:
            print(
                f"\nPlaying {card_1.name} with "
                f"{game_state['mana']} mana available:"
            )
            print(
                f"Playable: "
                f"{card_1.is_playable(game_state['mana'])}"
            )
            print(
                f"Play result: "
                f"{card_1.play(game_state)}\n"
            )
        except Exception as e:
            print(e)

        if card_2:
            print(f"{card_1.name} attacks {card_2.name}:")
            print(
                f"Attack result: "
                f"{card_1.attack_target(card_2)}\n"
            )

        try:
            game_state["mana"] = 3
            print(
                f"Testing insufficient mana "
                f"({game_state['mana']} available):"
            )
            print(
                f"Playable: "
                f"{card_1.is_playable(game_state['mana'])}\n"
            )
        except Exception as e:
            print(e)

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
