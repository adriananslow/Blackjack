import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        return [Card(suit, value) for suit in Card.SUIT_SYMBOLS for value in Card.VALUE_NAMES]

    def shuffle(self):
        rand_values = [random.random() for _ in range(52)]
        rand_deck = zip(self.cards, rand_values)
        shuffled_rand_deck = sorted(rand_deck, key = lambda x: x[1])
        self.cards = [item[0] for item in shuffled_rand_deck]

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
