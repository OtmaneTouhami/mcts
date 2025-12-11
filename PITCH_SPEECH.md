# 🎤 MCTS Tic-Tac-Toe: The "Global Pitch" Script

**Time Estimate:** 2-3 Minutes
**Goal:** Demonstrate AI decision-making transparency using the live demo.

---

### 1. The Hook (0:00 - 0:30)

"Good morning everyone. We've all played Tic-Tac-Toe. Usually, against a computer, it feels like a black box—it just beats you, and you don't know why.

Today, I'm demonstrating a **Monte Carlo Tree Search (MCTS)** engine. Unlike traditional AI that follows hard-coded 'if-then' rules, this AI **imagines the future**. It plays thousands of random games in its head to calculate the statistical probability of winning from any position."

### 2. The Live Demo (0:30 - 1:30)

_(Gesture to the screen)_
"Let's see it in action. I'll play as **X** (Human) and let the AI play as **O**."

**Step 1: The Opening (Easy Mode)**
"First, I'll select **Easy Mode**. This limits the AI's thinking time to just 1 second."
_(Select Easy Mode)_
"I'll start with the strongest move: **Center (1,1)**."
_(Play 1,1)_

"Watch the **AI Decision Insights** panel. Even in Easy mode, it runs thousands of simulations. It might make a mistake here because it hasn't explored enough possibilities."

**Step 2: The Mid-Game (Medium Mode)**
"Now, let's imagine we're in a tougher game. I'll switch to **Medium Mode** (3 seconds thinking time)."
_(Restart or pretend to switch context)_
"I'll try to set up a trap at **(2,2)**."
_(Play 2,2)_

"The AI responds instantly at **(0,0)**. Look at the data: it ran **50,000 simulations** this time. It realized that any other move would lower its win probability. It's adapting dynamically to my strategy."

### 3. The "Checkmate" (1:30 - 2:00)

"I'll make one last attempt to block at **(0,1)**."
_(Play 0,1)_

"Now, look at this specific insight. The AI ran nearly **200,000 simulations**.
See that **100% Win Rate** next to position **(1,0)**?
The AI has solved the game. It knows with absolute certainty that playing here guarantees a win."

_(AI plays 1,0 and wins)_

### 4. Conclusion (2:00 - 2:15)

"And there it is. The AI wins, but more importantly, we saw **how** it won.
This project isn't just about Tic-Tac-Toe; it's a demonstration of transparent, probability-based decision making. The AI doesn't need to be told the rules of strategy—it discovers them on its own, thousands of times per second.

Thank you!"
