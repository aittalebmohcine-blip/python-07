from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.split()[1].lower()}_{len(self.cards) + 1}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = card1_id if card1.rating > card2.rating else card2_id
        loser = card2_id if winner == card1_id else card1_id

        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)

        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.cards[winner].calculate_rating(),
            "loser_rating": self.cards[loser].calculate_rating(),
        }

    def get_leaderboard(self) -> list[dict]:
        def rating_key(card: TournamentCard) -> int:
            return card.calculate_rating()

        sorted_cards = sorted(
            list(self.cards.values()), key=rating_key, reverse=True
        )

        return [
            {
                "name": c.name,
                "rating": c.calculate_rating(),
                "record": f"{c.wins}-{c.losses}",
            }
            for c in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_matches = sum(
            c.wins + c.losses for c in self.cards.values()
            ) // 2
        avg_rating = (
            sum(
                c.calculate_rating() for c in self.cards.values()
                ) / total_cards
            if total_cards > 0
            else 0
        )

        return {
            "total_cards": total_cards,
            "matches_played": total_matches,
            "avg_rating": int(avg_rating),
            "platform_status": "active",
        }
