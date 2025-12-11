"""
Tic-Tac-Toe with Monte Carlo Tree Search (MCTS)
================================================
A complete implementation demonstrating MCTS algorithm for the presentation.
Human vs AI with decision insights shown after each AI move.

This is the main entry point that ties together the board and MCTS engine.
"""

from board import TicTacToeBoard
from mcts import MonteCarlo


# =============================================================================
# GAME INTERFACE - Human vs AI
# =============================================================================

def display_ai_insights(stats):
    """Display detailed AI decision insights."""
    print("\n" + "="*60)
    print("🤖 AI DECISION INSIGHTS")
    print("="*60)
    
    if stats.get('only_move'):
        print("Only one legal move available - no calculation needed.")
        return
    
    print(f"⏱️  Thinking time: {stats['time']}")
    print(f"🎲 Simulations run: {stats['simulations']:,}")
    print(f"🌳 Max tree depth: {stats['max_depth']}")
    print(f"⚖️  Exploration constant (C): {stats['exploration_constant']}")
    print()
    print("📊 MOVE ANALYSIS (sorted by win rate):")
    print("-"*60)
    print(f"{'Position':<10} {'Win Rate':<12} {'Wins':<10} {'Simulations':<12}")
    print("-"*60)
    
    for m in stats['move_analysis']:
        row, col = m['move'] // 3, m['move'] % 3
        pos_str = f"({row}, {col})"
        indicator = "👑" if m == stats['move_analysis'][0] else "  "
        print(f"{indicator} {pos_str:<8} {m['win_rate']:>6.2f}%     {m['wins']:<10} {m['plays']:<12}")
    
    print("-"*60)
    best = stats['move_analysis'][0]
    row, col = best['move'] // 3, best['move'] % 3
    print(f"\n✅ CHOSEN MOVE: Position ({row}, {col})")
    print(f"   Reason: Highest win rate of {best['win_rate']:.2f}% ")
    print(f"   Based on {best['plays']:,} simulations with {best['wins']:,} wins")
    print("="*60 + "\n")


def get_human_move(board, states):
    """Get a valid move from the human player."""
    legal = board.legal_plays(states)
    
    print("Your turn! Enter your move.")
    print("Available positions:", end=" ")
    for pos in legal:
        row, col = pos // 3, pos % 3
        print(f"({row},{col})", end=" ")
    print()
    
    while True:
        try:
            user_input = input("Enter row and column (e.g., '1 2' or '1,2'): ").strip()
            # Handle different input formats
            if ',' in user_input:
                row, col = map(int, user_input.split(','))
            else:
                row, col = map(int, user_input.split())
            
            move = row * 3 + col
            
            if move in legal:
                return move
            else:
                print("❌ Invalid move! That position is taken or out of bounds.")
        except (ValueError, IndexError):
            print("❌ Invalid input! Please enter row and column (0-2).")


def select_difficulty():
    """Let the user select AI difficulty level."""
    # Difficulty settings: (time in seconds, C exploration constant)
    difficulties = {
        '1': ('Easy',   1,  1.5),   # Short thinking, less exploration
        '2': ('Medium', 3,  2.5),   # Balanced
        '3': ('Hard',   6,  3.5),   # Long thinking, more exploration = unbeatable
    }
    
    print("\n🎯 SELECT DIFFICULTY:")
    print("   1. 😊 Easy   - AI thinks 1s (beatable)")
    print("   2. 🤔 Medium - AI thinks 3s (challenging)")
    print("   3. 💀 Hard   - AI thinks 6s (nearly unbeatable)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in difficulties:
            name, time_val, c_val = difficulties[choice]
            print(f"\n✅ Difficulty set to: {name}")
            return name, time_val, c_val
        print("Please enter 1, 2, or 3.")


def play_game():
    """Main game loop."""
    print("\n" + "="*60)
    print("   TIC-TAC-TOE with MCTS AI")
    print("   (Monte Carlo Tree Search Demonstration)")
    print("="*60)
    
    # Initialize
    board = TicTacToeBoard()

    # Select difficulty
    difficulty_name, thinking_time, exploration_constant = select_difficulty()
    
    # Configuration
    print("\n⚙️  AI Configuration:")
    print(f"   - Difficulty: {difficulty_name}")
    print(f"   - Thinking time: {thinking_time} seconds per move")
    print(f"   - Exploration constant (C): {exploration_constant}")
    
    # Choose who starts
    print("\n🎮 Who should start?")
    print("   1. Human (you play as X)")
    print("   2. AI (AI plays as X)")
    
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Please enter 1 or 2.")
    
    human_player = 1 if choice == '1' else 2
    ai_player = 2 if choice == '1' else 1
    
    player_symbols = {1: 'X', 2: 'O'}
    print(f"\n✅ You are playing as: {player_symbols[human_player]}")
    print(f"   AI is playing as: {player_symbols[ai_player]}")
    
    # Create AI with selected difficulty
    ai = MonteCarlo(board, time=thinking_time, C=exploration_constant)
    
    # Initialize game state
    state = board.start()
    states = [state]
    ai.update(state)
    
    # Game loop
    print("\n" + "-"*60)
    print("GAME START!")
    print("-"*60)
    board.display(state)
    
    while True:
        current_player = board.current_player(state)
        
        if current_player == human_player:
            # Human's turn
            print(f"👤 YOUR TURN ({player_symbols[human_player]})")
            move = get_human_move(board, states)
        else:
            # AI's turn
            print(f"🤖 AI THINKING ({player_symbols[ai_player]})...")
            move, stats = ai.get_play()
            display_ai_insights(stats)
        
        # Apply move
        state = board.next_state(state, move)
        states.append(state)
        ai.update(state)
        
        # Display board
        row, col = move // 3, move % 3
        player_name = "You" if current_player == human_player else "AI"
        print(f"📍 {player_name} played at position ({row}, {col})")
        board.display(state)
        
        # Check for winner
        winner = board.winner(states)
        if winner:
            print("="*60)
            if winner == -1:
                print("🤝 IT'S A TIE!")
            elif winner == human_player:
                print("🎉 CONGRATULATIONS! YOU WIN!")
            else:
                print("🤖 AI WINS! Better luck next time!")
            print("="*60)
            break
    
    # Play again?
    print("\nWould you like to play again? (y/n): ", end="")
    if input().strip().lower() == 'y':
        play_game()


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   MONTE CARLO TREE SEARCH (MCTS) DEMONSTRATION            ║
    ║   ─────────────────────────────────────────────           ║
    ║   This program demonstrates the MCTS algorithm            ║
    ║   playing Tic-Tac-Toe against a human player.             ║
    ║                                                           ║
    ║   After each AI move, you'll see detailed insights        ║
    ║   showing how the AI evaluated each possible move         ║
    ║   using the UCT (Upper Confidence bound for Trees)        ║
    ║   formula.                                                ║
    ║                                                           ║
    ║   The AI uses random simulations (rollouts) to            ║
    ║   estimate the win probability of each move.              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    play_game()
