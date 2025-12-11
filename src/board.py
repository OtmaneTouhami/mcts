"""
Tic-Tac-Toe Board Class
=======================
Encapsulates all the rules of Tic-Tac-Toe.
This is the game-specific implementation that the MCTS engine uses.
"""


class TicTacToeBoard:
    """
    Encapsulates all the rules of Tic-Tac-Toe.
    The state is represented as a tuple of 9 elements (0=empty, 1=X, 2=O).
    
    This class handles:
    - Game state representation
    - Legal move generation
    - Win condition checking
    - Board visualization
    """
    
    def start(self) -> tuple:
        """
        Returns the starting state of the game (empty board).
        
        Returns:
            tuple: A tuple of 9 zeros representing an empty 3x3 board.
        """
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    def current_player(self, state: tuple) -> int:
        """
        Returns the current player (1=X, 2=O) based on the board state.
        
        Args:
            state (tuple): The current board configuration.
            
        Returns:
            int: 1 for Player X, 2 for Player O.
        """
        # Count moves: if equal, it's player 1's turn (X)
        x_count = state.count(1)
        o_count = state.count(2)
        return 1 if x_count == o_count else 2
    
    def next_state(self, state: tuple, play: int) -> tuple:
        """
        Takes the game state and the move to be applied.
        Returns the new game state.
        
        Args:
            state (tuple): The current board configuration.
            play (int): The index (0-8) where the player wants to move.
            
        Returns:
            tuple: The new board configuration after the move.
        """
        state_list = list(state)
        player = self.current_player(state)
        state_list[play] = player
        return tuple(state_list)
    
    def legal_plays(self, state_history: list) -> list:
        """
        Returns the list of legal moves (empty positions).
        
        Args:
            state_history (list): A list of past game states (last one is current).
            
        Returns:
            list: A list of integers representing available board indices (0-8).
        """
        state = state_history[-1]
        return [i for i in range(9) if state[i] == 0]
    
    def winner(self, state_history: list) -> int:
        """
        Checks if the game has a winner.
        
        Args:
            state_history (list): A list of past game states.
            
        Returns:
            int: 
                1 if Player X wins
                2 if Player O wins
                -1 if it's a tie (draw)
                0 if the game is still ongoing
        """
        state = state_history[-1]
        
        # Winning combinations (indices)
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for line in lines:
            values = [state[i] for i in line]
            # Check if all cells in a line belong to the same non-empty player
            if values[0] != 0 and values[0] == values[1] == values[2]:
                return values[0]
        
        # Check for tie (no empty spaces left)
        if 0 not in state:
            return -1
        
        # Game ongoing
        return 0
    
    def display(self, state: tuple):
        """
        Pretty prints the board to the console.
        
        Args:
            state (tuple): The board configuration to display.
        """
        symbols = {0: ' ', 1: 'X', 2: 'O'}
        print()
        print("    0   1   2")
        print("  ┌───┬───┬───┐")
        for row in range(3):
            print(f"{row} │", end="")
            for col in range(3):
                idx = row * 3 + col
                print(f" {symbols[state[idx]]} │", end="")
            print()
            if row < 2:
                print("  ├───┼───┼───┤")
        print("  └───┴───┴───┘")
        print()
