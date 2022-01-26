import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        return [Card(suit, value) for suit in Card.SUIT_SYMBOLS for value in Card.VALUE_NAMES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
