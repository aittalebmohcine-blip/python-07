#   === DataDeck Tournament Platform ===
#
#   Registering Tournament Cards...
#
#   Fire Dragon (ID: dragon_001):
#   - Interfaces: [Card, Combatable, Rankable]
#   - Rating: 1200
#   - Record: 0-0
#
#   Ice Wizard (ID: wizard_001):
#   - Interfaces: [Card, Combatable, Rankable]
#   - Rating: 1150
#   - Record: 0-0
#
#   Creating tournament match...
#   Match result: {'winner': 'dragon_001', 'loser': 'wizard_001', 'winner_rating': 1216, 'loser_rating': 1134}
#
#   Tournament Leaderboard:
#   1. Fire Dragon - Rating: 1216 (1-0)
#   2. Ice Wizard - Rating: 1134 (0-1)
#
#   Platform Report:
#   {'total_cards': 2, 'matches_played': 1, 'avg_rating': 1175, 'platform_status': 'active'}
#
#   === Tournament Platform Successfully Deployed! ===
#   All abstract patterns working together harmoniously!


from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")
    try:
        dragon_001 = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
        wizard_001 = TournamentCard("Ice Wizard", 4, "Rare", 3, 4)
        platform = TournamentPlatform()
        platform.register_card(dragon_001)
        platform.register_card(wizard_001)
        cards = platform.cards
        for card in cards:
            print(f"\n{cards[card].name} (ID: {card}):")
            print(
                f"- Interfaces: {[c.__name__ for c in dragon_001.__class__.__bases__]}"
            )
            print(f"- Rating: {cards[card].rating}")
            print(f"- Record: {cards[card].wins}-{cards[card].losses})")

        print("\nCreating tournament match...")
        result = platform.create_match("dragon_1", "wizard_2")
        print(f"Match result: {result}")

        print("\nTournament Leaderboard:")
        i = 1
        for card in cards:
            name = cards[card].name
            rating = cards[card].rating
            wins = cards[card].wins
            losses = cards[card].losses
            print(f"{i}. {name} - Rating: {rating} ({wins}-{losses})")
            i += 1

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
