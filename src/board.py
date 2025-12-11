"""
Tic-Tac-Toe Board Class
=======================
Encapsulates all the rules of Tic-Tac-Toe.
This is the game-specific implementation that the MCTS engine uses.
"""


class TicTacToeBoard:
    """
    Encapsulates all the rules of Tic-Tac-Toe.
    The state is represented as a tuple of 9 elements (0=empty, 1=X, 2=O)
    """
    
    def start(self):
        """Returns the starting state of the game (empty board)."""
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    def current_player(self, state):
        """Returns the current player (1=X, 2=O)."""
        # Count moves: if equal, it's player 1's turn (X)
        x_count = state.count(1)
        o_count = state.count(2)
        return 1 if x_count == o_count else 2
    
    def next_state(self, state, play):
        """
        Takes the game state and the move to be applied.
        Returns the new game state.
        """
        state_list = list(state)
        player = self.current_player(state)
        state_list[play] = player
        return tuple(state_list)
    
    def legal_plays(self, state_history):
        """
        Returns the list of legal moves (empty positions).
        """
        state = state_history[-1]
        return [i for i in range(9) if state[i] == 0]
    
    def winner(self, state_history):
        """
        Returns the winner:
        - 1 if X wins
        - 2 if O wins
        - -1 if tie
        - 0 if game ongoing
        """
        state = state_history[-1]
        
        # Winning combinations
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for line in lines:
            values = [state[i] for i in line]
            if values[0] != 0 and values[0] == values[1] == values[2]:
                return values[0]
        
        # Check for tie (no empty spaces)
        if 0 not in state:
            return -1
        
        # Game ongoing
        return 0
    
    def display(self, state):
        """Pretty print the board."""
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
