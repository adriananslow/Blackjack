from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while True:
            if self.player.balance < self.MINIMUM_BET:
                print("You've ran out of money. Please restart this program to try again. Goodbye.")
                return

            while True:
                play_game_tag = input(f'You are starting with ${self.player.balance}. Would you like to play a hand? ').lower()
                if play_game_tag not in ['yes', 'no']:
                    print('That is not a valid option.')
                elif play_game_tag == 'no':
                    print(f'You left the game with ${self.player.balance}.')
                    return
                else:
                    break

            self.deck = Deck()
            self.deck.shuffle()

            while True:
                try:
                    self.bet = float(input('Place your bet: '))
                    if self.bet < Game.MINIMUM_BET:
                        print('The minimum bet is $1.')
                        continue
                    if self.bet > self.player.balance:
                        print('You do not have sufficient funds.')
                        continue
                    break
                except:
                    print('Incorrect value entered. Please try again.')
            
            self.player.hand = Hand()
            self.player.hand.add_to_hand(self.deck, 2)
            print(f'You are dealt: {str(self.player.hand)}')
            self.dealer.hand = Hand()
            self.dealer.hand.add_to_hand(self.deck, 2)
            print(f'The dealer is dealt: {str(self.dealer.hand)[:-2] + "Unknown"}')

            if self.player.hand.get_value() == 21:
                print(f'The dealer has: {str(self.dealer.hand)}')
                if self.dealer.hand.get_value() == 21:
                    print('You tie. Your bet has been returned.\n')
                else:
                    print(f'Blackjack! You win ${self.bet * 1.5} :)')
                    self.player.balance += self.bet * 1.5
                continue

            while True:
                hit_stay_tag = input('Would you like to hit or stay? ').lower()
                if hit_stay_tag == 'hit':
                    self.player.hand.add_to_hand(self.deck, 1)
                    print(f'You now have: {str(self.player.hand)}')
                    if self.player.hand.get_value() > 21:
                        print(f'Your hand value is over 21 and you lose ${self.bet} :(\n')
                        self.player.balance -= self.bet
                        break
                elif hit_stay_tag == 'stay':
                    break
            
            if self.player.hand.get_value() > 21:
                continue

            print(f'The dealer has: {str(self.dealer.hand)}')
            while True:
                if self.dealer.hand.get_value() > 21:
                    print(f'The dealer busts, you win ${self.bet} :)')
                    self.player.balance += self.bet
                    break
                elif self.dealer.hand.get_value() < 17:
                    self.dealer.hand.add_to_hand(self.deck, 1)
                    print(f'The dealer hits and is dealt: {str(self.dealer.hand)[-2:]}')
                    print(f'The dealer now has: {str(self.dealer.hand)}')
                else:
                    print('The dealer stays.')
                    if self.player.hand.get_value() > self.dealer.hand.get_value():
                        print(f'You win ${self.bet}!\n')
                        self.player.balance += self.bet
                        break
                    if self.player.hand.get_value() == self.dealer.hand.get_value():
                        print('You tie. Your bet has been returned.\n')
                        break
                    if self.player.hand.get_value() < self.dealer.hand.get_value():
                        print(f'The dealer wins, you lose ${self.bet} :(\n')
                        self.player.balance -= self.bet
                        break
