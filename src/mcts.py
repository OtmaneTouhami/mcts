"""
Monte Carlo Tree Search (MCTS) Engine
=====================================
A game-agnostic MCTS implementation with UCT (Upper Confidence bound for Trees).
This is the AI brain that uses random simulations to find the best move.

Based on Jeff Bradberry's MCTS tutorial structure.
"""

import math
import random
import time


class MonteCarlo:
    """
    Monte Carlo Tree Search with UCT (Upper Confidence bound for Trees).
    This is the AI brain that uses random simulations to find the best move.
    
    The algorithm proceeds in four phases:
    1. Selection: Traverse the tree to find a leaf node using UCT.
    2. Expansion: Add a new child node to the tree.
    3. Simulation: Perform a random rollout from the new node to a terminal state.
    4. Backpropagation: Update the stats (wins/plays) back up the tree.
    """
    
    def __init__(self, board, **kwargs):
        """
        Initialize the MCTS engine.
        
        Args:
            board: The game board object (must implement start, current_player, next_state, legal_plays, winner).
            **kwargs: Configuration options:
                - time (int): Max calculation time in seconds (default: 2).
                - max_moves (int): Max depth for simulations (default: 9).
                - C (float): Exploration constant for UCT (default: 1.4).
        """
        self.board = board
        self.states = []
        
        # Configuration
        self.calculation_time = kwargs.get('time', 2)  # seconds
        self.max_moves = kwargs.get('max_moves', 9)
        
        # The exploration constant (C in UCT formula)
        # Higher = more exploration (trying new moves)
        # Lower = more exploitation (sticking to known good moves)
        self.C = kwargs.get('C', 1.4)
        
        # Statistics tables
        self.wins = {}   # wins[(player, state)] = number of wins
        self.plays = {}  # plays[(player, state)] = number of plays
        
        # For insights
        self.max_depth = 0
        self.last_stats = {}
    
    def update(self, state: tuple):
        """
        Appends the state to the game history.
        
        Args:
            state (tuple): The new game state to append.
        """
        self.states.append(state)
    
    def get_play(self) -> tuple:
        """
        Calculates the best move from the current game state.
        
        Returns:
            tuple: (best_move_index, statistics_dict)
        """
        self.max_depth = 0
        state = self.states[-1]
        player = self.board.current_player(state)
        legal = self.board.legal_plays(self.states[:])
        
        # Bail out early if there's no choice
        if not legal:
            return None, {}
        if len(legal) == 1:
            return legal[0], {"only_move": True}
        
        # Run simulations for the configured time
        games = 0
        begin = time.time()
        while time.time() - begin < self.calculation_time:
            self.run_simulation()
            games += 1
        
        elapsed = time.time() - begin
        
        # Collect statistics for each possible move
        moves_states = [(p, self.board.next_state(state, p)) for p in legal]
        
        # Calculate win rates for all moves
        move_stats = []
        for move, S in moves_states:
            wins = self.wins.get((player, S), 0)
            plays = self.plays.get((player, S), 1)
            win_rate = wins / plays if plays > 0 else 0
            move_stats.append({
                'move': move,
                'wins': wins,
                'plays': plays,
                'win_rate': win_rate * 100
            })
        
        # Sort by win rate
        move_stats.sort(key=lambda x: x['win_rate'], reverse=True)
        
        # Pick the move with the highest win percentage
        best_move = move_stats[0]['move']
        
        # Store insights
        self.last_stats = {
            'simulations': games,
            'time': f"{elapsed:.2f}s",
            'max_depth': self.max_depth,
            'move_analysis': move_stats,
            'exploration_constant': self.C
        }
        
        return best_move, self.last_stats
    
    def run_simulation(self):
        """
        Runs one complete MCTS simulation:
        1. Selection (using UCB1)
        2. Expansion
        3. Simulation (random rollout)
        4. Backpropagation
        """
        plays, wins = self.plays, self.wins
        
        visited_states = set()
        states_copy = self.states[:]
        state = states_copy[-1]
        player = self.board.current_player(state)
        
        expand = True
        
        for t in range(1, self.max_moves + 1):
            legal = self.board.legal_plays(states_copy)
            
            if not legal:
                break
            
            moves_states = [(p, self.board.next_state(state, p)) for p in legal]
            
            # =========================================================
            # PHASE 1: SELECTION (using UCB1/UCT)
            # =========================================================
            if all(plays.get((player, S)) for p, S in moves_states):
                # We have stats on all legal moves - use UCT formula
                log_total = math.log(
                    sum(plays[(player, S)] for p, S in moves_states)
                )
                
                # UCT = win_rate + C * sqrt(ln(N) / n)
                # This balances exploitation (win_rate) and exploration (sqrt term)
                value, move, state = max(
                    (
                        (wins[(player, S)] / plays[(player, S)]) +  # Exploitation
                        self.C * math.sqrt(log_total / plays[(player, S)]),  # Exploration
                        p, 
                        S
                    )
                    for p, S in moves_states
                )
            else:
                # =========================================================
                # PHASE 3: SIMULATION (random rollout)
                # =========================================================
                # Not all moves have stats - pick randomly
                move, state = random.choice(moves_states)
            
            states_copy.append(state)
            
            # =========================================================
            # PHASE 2: EXPANSION
            # =========================================================
            # Add new node to the tree
            if expand and (player, state) not in plays:
                expand = False
                plays[(player, state)] = 0
                wins[(player, state)] = 0
                if t > self.max_depth:
                    self.max_depth = t
            
            visited_states.add((player, state))
            
            player = self.board.current_player(state)
            winner = self.board.winner(states_copy)
            if winner:
                break
        
        # =========================================================
        # PHASE 4: BACKPROPAGATION
        # =========================================================
        # Update statistics for all visited states
        for player, state in visited_states:
            if (player, state) not in plays:
                continue
            plays[(player, state)] += 1
            if player == winner:
                wins[(player, state)] += 1
