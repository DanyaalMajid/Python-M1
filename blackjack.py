from os import system, name
import random

class blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False
        self.deal_cards()

    def create_deck(self):
        # Create a deck of cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck
    
    def deal_cards(self):
        # Deal two cards to the player and dealer
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.calculate_score()

    def calculate_score(self):
        # Calculate the score of the player and dealer
        self.player_score = self.get_score(self.player_hand)
        self.dealer_score = self.get_score(self.dealer_hand)

    def get_score(self, hand):
        # Get the score of a hand
        score = 0
        num_aces = 0
        for card in hand:
            rank = card['rank']
            if rank in ['Jack', 'Queen', 'King']:
                score += 10
            elif rank == 'Ace':
                score += 11
                num_aces += 1
            else:
                score += int(rank)
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score
    

    def clear_screen(self):
        # Clear the screen
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def print_board(self, show_dealer_hand=False):
        # Print the game board
        self.clear_screen()
        print("Player's Hand:")
        for card in self.player_hand:
            print(f"{card['rank']} of {card['suit']}")
        print(f"Score: {self.player_score}")
        print("\nDealer's Hand:")
        if show_dealer_hand:
            for card in self.dealer_hand:
                print(f"{card['rank']} of {card['suit']}")
            print(f"Score: {self.dealer_score}")
        else:
            print(f"{self.dealer_hand[0]['rank']} of {self.dealer_hand[0]['suit']}")
            print("Hidden card")

    def player_turn(self):
        # Player's turn
        while True:
            self.print_board()
            if self.player_score == 21:
                print("Blackjack! You win!")
                self.game_over = True
                break
            elif self.player_score > 21:
                print("Bust! You lose!")
                self.game_over = True
                break
            else:
                choice = input("Do you want to hit or stand? (h/s): ")
                if choice == 'h':
                    self.player_hand.append(self.deck.pop())
                    self.calculate_score()
                else:
                    break

    def dealer_turn(self):
        # Dealer's turn
        while self.dealer_score < 17:
            self.dealer_hand.append(self.deck.pop())
            self.calculate_score()
        self.print_board(show_dealer_hand=True)
        if self.dealer_score == 21:
            print("Blackjack! Dealer wins!")
        elif self.dealer_score > 21:
            print("Bust! Dealer loses!")
        elif self.dealer_score > self.player_score:
            print("Dealer wins!")
        elif self.dealer_score < self.player_score:
            print("Player wins!")
        else:
            print("It's a tie!")
        self.game_over = True

    def play_game(self):
        # Main game loop
        while not self.game_over:
            self.player_turn()
            if not self.game_over:
                self.dealer_turn()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            self.__init__()
            self.play_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    game = blackjack()
    game.play_game()
    