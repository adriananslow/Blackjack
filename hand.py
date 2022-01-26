class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self):
        value = 0
        card_values = [str(card)[1] for card in self.cards]
        for card_value in card_values:
            if card_value in ['T', 'J', 'Q', 'K']:
                value += 10
            elif card_value == 'A':
                value += 11
            else:
                value += int(card_value)
        if value > 21 and 'A' in card_values:
            value -= 10
        return value
        
    def add_to_hand(self, deck, num_cards):
        self.cards += deck.deal(num_cards)

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
