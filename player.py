class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = None

    def get_str_hand(self, hand):
        return hand.str()
