# SUGGESTED_PITCH.md

## General Speaking Tips
- **Duration Goal:** 40+ Minutes (approx. 8 minutes per speaker).
- **Pacing:** Slow down. Don't just read. Explain, pause, ask questions, and let the concepts sink in.
- **Interaction:** We have added specific questions to ask the audience to burn time and check understanding.

---

## Clown N°1: The Context & The "Why"
**(Slides 1-4)**

**Slide 1: Title**
"Good morning everyone. Today, we are going to explore the engine behind one of the greatest breakthroughs in computer science history.
We are talking about **Monte Carlo Tree Search (MCTS)**.
It sounds like a mouthful, but by the end of this hour, you will understand that it is actually a very simple, beautiful idea. It is the story of how we taught computers to 'think' like humans—not by calculating everything, but by using **intuition** and **randomness**."

**Slide 2: Agenda**
"We have a lot to cover, so we’ve broken it down into 5 distinct parts, each led by one of us:
1.  **I (Clown N°1)** will set the stage. Why did the old AI stop working? Why do we need MCTS?
2.  **Clown N°2** will take you inside the machine to see the 4-step life cycle of the algorithm.
3.  **Clown N°3** will be our mathematician. He will explain the 'brain'—the formula that balances curiosity and greed.
4.  **Clown N°4** will translate that math into Python code.
5.  **Clown N°5** will show you the AI in action and connect it to the famous AlphaGo victory."

**Slide 3: The Explosion Problem (Deep Dive)**
"Let's go back in time. 1997. Deep Blue beats Kasparov at Chess. Everyone thought AI was solved.
But for 20 years, AI couldn't beat a professional at **Go**. Why?
*(Pause for audience guess)*
It’s the **Branching Factor**.
In Chess, on any given turn, you have about 35 legal moves.
In Go, you have 250.
Let's do the math. If you want to look just 3 moves ahead:
- Chess: $35 \times 35 \times 35 \approx 42,000$ positions. Manageable.
- Go: $250 \times 250 \times 250 \approx 15,000,000$ positions.
And a game of Go lasts 200 moves. The number of possibilities is greater than the number of atoms in the universe.
**Minimax**, the old algorithm, tries to see everything. In Go, Minimax crashes immediately. We hit a wall."

**Slide 4: The Monte Carlo Intuition (The Metaphor)**
"So, if we can't calculate everything, what do we do? We guess. But we guess smartly.
Imagine you are a tourist in a new city. You want to find the best restaurant.
**Method A (Minimax):** You walk into *every* restaurant in the city, try *every* dish, and then decide. You will die of old age before you eat dinner.
**Method B (Monte Carlo):** You stand in the square and pick 5 random people. You ask them: 'Did you like the food?'
If 4 out of 5 say 'It was amazing,' you can be pretty sure it's good.
Did you test everything? No.
Are you 100% sure? No.
But is it 'good enough' to make a decision? **Yes.**
This is the revolution. MCTS uses **random sampling** to approximate the truth. We play thousands of random games to guess which move is best."

---

## Clown N°2: The Mechanism (The 4 Steps)
**(Slides 5-7)**

**Slide 5: The Cycle**
"Thanks, Clown N°1. So, we know *why* we use randomness. Now let's see *how* we organize it.
MCTS isn't magic. It's a loop. A cycle that repeats over and over again—sometimes 10,000 times before the computer makes a single move.
It has exactly 4 steps. I want you to memorize these: **Selection, Expansion, Simulation, Backpropagation.**"

**Slide 6: Selection & Expansion (Walkthrough)**
"Let's imagine a tree.
**Step 1: Selection.**
We start at the Root. We need to go down. But which way?
We don't pick randomly here. We pick the path that looks the most promising *so far*. We follow the 'signposts' (the stats) down the tree until we hit a leaf node—a place where we haven't explored yet.
**Step 2: Expansion.**
We are at the edge of the known world. We want to see what's next. So we add **one new node**.
*(Point to slide)*
We literally create a new child object in memory. The tree just got bigger by one step."

**Slide 7: Simulation & Backpropagation (The Crucial Part)**
"Now, pay attention. This is the unique part of MCTS.
**Step 3: Simulation (The Rollout).**
We are at this new node. We have no idea if it's good or bad. How do we find out?
We play a game. But not a smart game. We play a **random** game.
We simulate moves—Black, White, Black, White—picking randomly until the game ends.
Why random? Because it's **fast**. We can play a whole game in microseconds.
Let's say Black wins.
**Step 4: Backpropagation.**
We have a result: 'Black Won'.
Now we have to tell the tree. We walk back up the path we came from—from the leaf all the way to the root.
We tell every node: 'Hey, I just visited your child, and it led to a Win.'
So we increment their 'Visits' count and their 'Wins' count.
The next time we come down, this path will look a little bit better.
This loop happens thousands of times. Slowly, the 'random' noise cancels out, and the 'good' moves rise to the top."

---

## Clown N°3: The Mathematics (UCT)
**(Slides 8-9)**

**Slide 8: The Dilemma**
"Thank you, Clown N°2.
Now, I have a question for the class.
In Step 1 (Selection), how do we decide which child to pick?
Imagine you have two slot machines.
- Machine A: You played it 2 times, and won 2 times. (100% win rate).
- Machine B: You played it 100 times, and won 60 times. (60% win rate).
Which one do you play next?
*(Wait for answers)*
If you pick A, you are **Exploiting**. You are greedy. But maybe A just got lucky?
If you pick B, you are **Exploring**. You are gathering more data on the 'safe' bet.
This is the **Exploration vs. Exploitation Dilemma**.
If we only exploit, we get stuck in local traps. If we only explore, we never play the best move."

**Slide 9: The UCT Formula (The Math)**
"To solve this, we use the **Upper Confidence Bound for Trees (UCT)**.
*(Write on board or point to slide)*
$$UCT = \frac{w_i}{n_i} + C \sqrt{\frac{\ln N_i}{n_i}}$$
Let's deconstruct this. It's not scary. It's just two parts fighting each other.
**Part 1: The Greedy Part ($\frac{w}{n}$)**
This is just your win percentage. If you won 8 out of 10 games, this is 0.8.
This term wants you to pick the 'best' move.
**Part 2: The Curious Part ($\sqrt{\dots}$)**
This is the exploration term.
Look at the denominator: $n_i$ (visits to the child). It's on the bottom.
What happens if $n_i$ is small (we haven't visited this node much)?
The number becomes **HUGE**.
So, if a node is ignored, this term grows and grows until it screams: 'PICK ME! I'M UNEXPLORED!'
**The Constant C:**
This $C$ is the balance. Usually $\sqrt{2}$.
- High C = The AI is a curious explorer (tries everything).
- Low C = The AI is a greedy master (sticks to what it knows).
This one formula solves the dilemma perfectly."

---

## Clown N°4: The Implementation (Python)
**(Slides 10-11)**

**Slide 10: The Architecture**
"Alright, math is great, but we are engineers. Let's see the code.
We are going to implement this in Python. We need two main classes.
**1. The `MCTSNode` Class:**
Think of this as a container. It needs to store:
- `self.state`: What the board looks like.
- `self.parent`: Who created me?
- `self.children`: Who comes next?
- `self.visits`: How many times have we been here? ($n$)
- `self.wins`: How many times did we win? ($w$)
**2. The `MCTS` Class:**
This is the runner. It just loops."

**Slide 11: The Code Logic (Deep Dive)**
"I want to show you the two most critical functions.
**First: The Rollout (Simulation).**
```python
def rollout(self, state):
    while not state.is_game_over():
        possible_moves = state.get_legal_moves()
        action = random.choice(possible_moves)
        state = state.move(action)
    return state.get_result()
```
Look at how simple this is. `random.choice()`. That's it. No heuristics. No evaluation function. Just random chaos.
**Second: The Selection (UCT).**
```python
def best_child(self, node):
    choices_weights = [
        (child.wins / child.visits) + 
        1.41 * math.sqrt((math.log(node.visits) / child.visits))
        for child in node.children
    ]
    return node.children[np.argmax(choices_weights)]
```
This is the direct translation of Clown N°3's formula.
We calculate the score for every child, and we pick the max.
If we run this loop 1000 times, the tree naturally grows towards the winning paths."

---

## Clown N°5: Demo & Conclusion
**(Slides 12-14)**

**Slide 12: Live Demo**
"Okay, moment of truth.
*(Open Terminal)*
I have a script here implementing MCTS for Connect 4 (or Tic-Tac-Toe).
I'm going to set the simulations to 1000.
*(Run Game)*
I'll play column 3.
Watch the terminal. You see those numbers scrolling? That's the loop: Selection, Expansion, Simulation, Backpropagation.
It just played 1000 games in 0.5 seconds.
It decided to block me.
Now, let's lower the simulations to 10.
*(Run Game with 10 sims)*
See? It plays instantly, but it plays poorly. It makes mistakes.
This proves that **Intelligence comes from the quantity of simulations**."

**Slide 13: The AlphaGo Connection**
"You might ask: 'Is this really how AlphaGo beat Lee Sedol?'
Yes and No.
AlphaGo used MCTS. It used the exact same tree structure.
But for the **Rollout**, instead of playing *completely* randomly, it used a Neural Network to guide the randomness.
And for the **Selection**, it used another Neural Network to help the UCT formula.
But the heart of the system was still this Tree Search."

**Slide 14: Conclusion**
"To wrap up:
1.  **Minimax** failed because the world is too big (Branching Factor).
2.  **MCTS** succeeds because it samples the world instead of mapping it.
3.  **UCT** is the math that balances our curiosity with our greed.
4.  And the code is surprisingly simple—random loops creating intelligent behavior.
MCTS teaches us that you don't need to know everything to make the right decision. You just need to explore enough possibilities to be confident.
Thank you for listening. We are now open for questions."
