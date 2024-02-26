from os import system, name
import random

class blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.player_money = 0
        self.player_bet_amount = 0
        self.dealer_score = 0
        self.game_over = False
        self.deal_cards()

    def new_game_init(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.player_bet_amount = 0
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
        print(f"Money: {self.player_money}")
        print(f"Bet: {self.player_bet_amount}")
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
                self.player_money += self.player_bet_amount * 2
                self.player_bet_amount = 0
                self.game_over = True
                break
            elif self.player_score > 21:
                print("Bust! You lose!")
                self.player_bet_amount = 0
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
            self.player_bet_amount = 0
        elif self.dealer_score > 21:
            print("Bust! Dealer loses!")
            self.player_money += self.player_bet_amount * 2
            self.player_bet_amount = 0
        elif self.dealer_score > self.player_score:
            print("Dealer wins!")
            self.player_bet_amount = 0
        elif self.dealer_score < self.player_score:
            print("Player wins!")
            self.player_money += self.player_bet_amount * 2
            self.player_bet_amount = 0
        else:
            print("It's a tie!")
            self.player_money += self.player_bet_amount
            self.player_bet_amount = 0
        self.game_over = True

    def player_intial_bet(self):
        self.player_money = int(input("Enter the amount of money you want to start with: "))
        self.player_bet()

    def player_bet(self):
        print(f"Your current money: {self.player_money}")
        self.player_bet_amount = int(input("Enter the amount of money you want to bet: "))
        if self.player_bet_amount > self.player_money:
            print("You don't have enough money to bet that amount!")
            self.player_bet()

        else:
            self.player_money -= self.player_bet_amount

    def play_game(self, new_game=True):
        # Main game loop
        if new_game == True:
            self.player_intial_bet()
        else:
            self.player_bet()

        while not self.game_over:
            self.player_turn()
            if not self.game_over:
                self.dealer_turn()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            self.new_game_init()  # Reset game except player_money
            self.play_game(new_game=False)  # Start a new game
        else:
            print("Thanks for playing!")
            print(f"Your final money: {self.player_money}")

if __name__ == "__main__":
    game = blackjack()
    game.play_game()
    