from os import system, name

class TicTacToe:
    def __init__(self):
        # Initialize the game board
        self.rows = 3
        self.cols = 3
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'
    
    def print_board(self):
        # Print the current state of the game board
        print("-" * 13)
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("-" * 13)
    
    def make_move(self, row, col):
        # Make a move on the game board
        if self.board[row][col] != " ":
            print("That spot is already taken!")
            return False  # Return False to indicate that the move was not successful
        else:
            self.board[row][col] = self.current_player
            return True  # Return True to indicate that the move was successful

        
    
    def check_winner(self):
        # Check if there is a winner
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
            all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
        all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False
    
    def is_board_full(self):
        # Check if the game board is full
        if all(all(cell != " " for cell in row) for row in self.board):
            self.clear_screen()
            self.print_board()
            print("It's a tie!")
            return True
        
    
    def switch_player(self):
        # Switch the current player
        switch = {
            'X': 'O',
            'O': 'X'
        }
        self.current_player = switch[self.current_player]

    def clear_screen(self):
        # Clear the screen
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
        

    def play_game(self):
        # Main game loop
        while True:
            self.clear_screen()
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            
            while True:
                row = int(input(f"Enter the row (1, 2, 3): "))
                col = int(input("Enter the column (1, 2, 3): "))
                
                if row not in [1, 2, 3] or col not in [1, 2, 3]:
                    print("Invalid input!")
                    continue
                
                row -= 1
                col -= 1
                
                if self.make_move(row, col):
                    break  # Break out of the loop if the move is successful

            if self.check_winner():
                self.clear_screen()
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_board_full():
                break
            self.switch_player()


if __name__ == "__main__":
    # Create an instance of the TicTacToe class and play the game
    TicTacToe().play_game()
