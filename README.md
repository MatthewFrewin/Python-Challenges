# Python Challenges
A set of challenges to refresh my knowledge of Python while building some fun and/or useful projects.

Note: I asked ChatGPT to generate these challenges using this prompt:
Set of challenges of increasing difficulty, starting off quite simple. The aim is to learn Python (I've used it once or twice before and also am experienced with other languages such as C#). A good mix of useful tools and/or things with a game dev twist or AI (or AI in Game Dev!). I'd like the first challenges to be completable within a short time, maybe less than 1-2 hours. As the projects get more complex, they can take more time to complete but I'd rather they never take more than a day at this point.

---

Level 1: Getting Started with Python Basics

1️⃣ Print a Simple ASCII Dungeon!

    Write a Python script that prints a simple ASCII dungeon layout using print().

    Example:

#####
# @ #
#   #
#####

🏆 Bonus: Make it more dynamic by using variables for width/height.

2️⃣ Simple Dice Roller 🎲

    Write a Python function that simulates rolling a 6-sided die.

    Use the random module to generate a random number between 1 and 6.

    🏆 Bonus: Allow rolling different types of dice (d20, d100, etc.).

Level 2: Intro to Game Logic & Objects

3️⃣ Basic Character Class

    Create a Character class with attributes like name, health, and strength.

    Implement a take_damage(amount) method that reduces health.

    🏆 Bonus: Add an attack(target) method that deals damage to another character.

4️⃣ Text-Based Battle Simulation

    Use your Character class to create a simple 1v1 battle loop.

    Each turn, characters attack each other until one reaches 0 health.

    🏆 Bonus: Add critical hits (e.g., 10% chance to deal double damage).

Level 3: Algorithms & Procedural Generation

5️⃣ Random Dungeon Generator 🏰

    Generate a 2D grid of . (floor) and # (walls).

    Randomly place an @ (player) somewhere.

    🏆 Bonus: Use cellular automata or a BSP algorithm for a more natural look.

6️⃣ Pathfinding: Implement A Algorithm*

    Given a grid-based map with obstacles (#), implement A* to find a path from @ to X.

    🏆 Bonus: Visualize the search process in ASCII.

Level 4: Game AI & Behavior Trees

7️⃣ Basic Enemy AI (Finite State Machine - FSM)

    Create an enemy that switches between Idle, Patrolling, and Chasing states.

    🏆 Bonus: Implement a "hearing" mechanic (reacting to nearby sounds).

8️⃣ Flocking AI (Boids Algorithm) 🦅

    Simulate a flock of birds (or enemies) moving together using three simple rules:

        Cohesion (stick together)

        Alignment (move in the same direction)

        Separation (avoid colliding with neighbors)

    🏆 Bonus: Render with pygame for a visual representation.

Level 5: AI for Game Dev

9️⃣ Neural Network for Enemy Decision-Making (Basic AI Brain!)

    Train a simple neural network using numpy or pytorch to make basic fight-or-flight decisions based on input variables (e.g., player distance, health).

    🏆 Bonus: Evolve the AI using genetic algorithms!

🔟 Reinforcement Learning for Game AI (Q-Learning / DQN)

    Train an AI to navigate a simple maze using reinforcement learning (Q-learning).

    🏆 Bonus: Train an AI-controlled character to learn combat strategies!