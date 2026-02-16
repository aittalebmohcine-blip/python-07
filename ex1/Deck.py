from ex0.Card import Card
import random


# Deck (Management Class)
class Deck:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("[LOGIC ERROR]: The card argument must be a Card instance.")
        if card in self.deck:
            raise ValueError("[LOGIC ERROR]: Cannot add existing cards to the deck.")
        else:
            self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str):
            raise TypeError("[LOGIC ERROR]: The card_name argument must be a string.")
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if not self.deck:
            raise ValueError("[LOGIC ERROR]: Deck is empty, cannot draw a card.")
        return self.deck.pop(-1)

    # Deck stats: {'total_cards': 3, 'creatures': 1, 'spells': 1, 'artifacts': 1, 'avg_cost': 4.0}
    def get_deck_stats(self) -> dict:
        avg_cost = (
            0
            if not self.deck
            else (sum(card.cost for card in self.deck) / len(self.deck))
        )
        return {
            "total_cards": len(self.deck),
            "creatures": len(
                [card for card in self.deck if getattr(card, "type", "") == "Creature"]
            ),
            "spells": len(
                [card for card in self.deck if getattr(card, "type", "") == "Spell"]
            ),
            "artifacts": len(
                [card for card in self.deck if getattr(card, "type", "") == "Artifact"]
            ),
            "avg_cost": round(avg_cost, 2),
        }
