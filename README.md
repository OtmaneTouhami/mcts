# 🎮 Monte Carlo Tree Search (MCTS) - Tic-Tac-Toe Demo

A complete implementation of the **Monte Carlo Tree Search** algorithm with **UCT (Upper Confidence bound for Trees)** demonstrated through an interactive Tic-Tac-Toe game.

This project was created for an educational presentation on MCTS algorithms.

---

## 📖 What is MCTS?

Monte Carlo Tree Search is an AI algorithm that uses **random simulations** to find the best move in a game. Instead of calculating every possible outcome (like Minimax), MCTS:

1. **Selection** - Navigate the tree using UCT formula to balance exploration vs exploitation
2. **Expansion** - Add a new node to the tree
3. **Simulation** - Play random moves until the game ends
4. **Backpropagation** - Update win/loss statistics back up the tree

### The UCT Formula

$$UCT = \frac{w_i}{n_i} + C \sqrt{\frac{\ln N}{n_i}}$$

Where:

- $w_i$ = wins for this node
- $n_i$ = simulations for this node
- $N$ = total simulations for parent
- $C$ = exploration constant (typically 1.4)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No external dependencies required!

### Run the Game

```bash
# Clone the repository
git clone <your-repo-url>
cd MCTS

# Run the game
python3 src/main.py
```

---

## 🎯 How to Play

1. Run the game with `python3 src/main.py`
2. Choose who starts:
   - **Option 1**: Human plays first (as X)
   - **Option 2**: AI plays first (as X)
3. Enter moves as row and column: `1 1` or `1,1`
4. Watch the AI's decision insights after each move!

### Example Gameplay

```
    0   1   2
  ┌───┬───┬───┐
0 │ X │   │   │
  ├───┼───┼───┤
1 │   │ O │   │
  ├───┼───┼───┤
2 │   │   │   │
  └───┴───┴───┘
```

---

## 🤖 AI Decision Insights

After each AI move, you'll see detailed statistics:

```
============================================================
🤖 AI DECISION INSIGHTS
============================================================
⏱️  Thinking time: 2.00s
🎲 Simulations run: 15,780
🌳 Max tree depth: 9
⚖️  Exploration constant (C): 1.4

📊 MOVE ANALYSIS (sorted by win rate):
------------------------------------------------------------
Position   Win Rate     Wins       Simulations
------------------------------------------------------------
👑 (1, 1)    85.63%     11368      13276
   (0, 0)    57.14%     196        343
   (2, 2)    58.71%     236        402
------------------------------------------------------------

✅ CHOSEN MOVE: Position (1, 1)
   Reason: Highest win rate of 85.63%
   Based on 13,276 simulations with 11,368 wins
============================================================
```

---

## 📁 Project Structure

```
MCTS/
├── src/
│   ├── board.py          # TicTacToeBoard class (game rules)
│   ├── mcts.py           # MonteCarlo class (MCTS/UCT algorithm)
│   └── main.py           # Game interface & entry point
├── PLAN.md               # Presentation planning document
├── SELF_STUDY_GUIDE.md   # Learning resources for MCTS
├── SLIDES_SUGGESTED_CONTENT.md  # Slide content suggestions
├── SUGGESTED_PITCH.md    # Presentation speech/pitch
└── README.md             # This file
```

### Module Descriptions

| File           | Description                                                                   |
| -------------- | ----------------------------------------------------------------------------- |
| `src/board.py` | Encapsulates Tic-Tac-Toe rules. Implements the game interface that MCTS uses. |
| `src/mcts.py`  | Game-agnostic MCTS engine. Contains the UCT algorithm and simulation logic.   |
| `src/main.py`  | Human vs AI game loop with move input and insight display.                    |

---

## ⚙️ Configuration

You can modify AI behavior in `src/main.py`:

```python
ai = MonteCarlo(board, time=2, C=1.4)
```

| Parameter   | Default | Description                                     |
| ----------- | ------- | ----------------------------------------------- |
| `time`      | 2       | Thinking time in seconds per move               |
| `C`         | 1.4     | Exploration constant. Higher = more exploration |
| `max_moves` | 9       | Maximum moves per simulation                    |

---

## 📚 Learning Resources

See [SELF_STUDY_GUIDE.md](SELF_STUDY_GUIDE.md) for:

- Video tutorials (Computerphile, etc.)
- Articles with diagrams
- Interactive visualizers
- UCT formula explanations

---

## 🎓 Presentation Materials

This project includes presentation preparation materials:

- **[PLAN.md](PLAN.md)** - Overall presentation structure
- **[SLIDES_SUGGESTED_CONTENT.md](SLIDES_SUGGESTED_CONTENT.md)** - Slide-by-slide content
- **[SUGGESTED_PITCH.md](SUGGESTED_PITCH.md)** - Speaker notes and explanations

---

## 🔧 Extending to Other Games

The MCTS engine (`src/mcts.py`) is **game-agnostic**. To use it with another game:

1. Create a new board class implementing these methods:

   - `start()` - Initial game state
   - `current_player(state)` - Who's turn
   - `next_state(state, play)` - Apply a move
   - `legal_plays(state_history)` - Available moves
   - `winner(state_history)` - Check for winner

2. Pass your board to `MonteCarlo(your_board)`

---

## 📄 License

This project is for educational purposes.

---

## 🙏 Credits

- Based on [Jeff Bradberry's MCTS Tutorial](https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/)
- UCT algorithm from Kocsis & Szepesvári (2006)
