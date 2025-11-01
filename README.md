# Flappy Bird AI

This project trains a very small neural-network–based agent to play a simplified Flappy Bird clone implemented with Pygame. It is an experimental, minimal example showing how a population of simple agents can be mutated and selected over generations to improve performance at a game task.

What it is
- A playable Flappy Bird-style environment (rendered with Pygame) with pairs of vertical "tubes" moving left.
- A population of birds (agents). Each bird has a tiny neural network ("brain") that takes a few numeric inputs describing the current state and outputs a single value that determines whether the bird jumps.
- A basic evolutionary loop: each generation the population is cloned from the current best agent, small random perturbations are applied to weights, the population is evaluated in the environment, and the best-performing agent is kept for the next generation.
- This repository is an educational toy demonstrating the core ideas of population-based search / neuroevolution in a very small codebase.

What it is NOT
- It is not a production-ready reinforcement learning framework.
- The neural network is tiny (4 inputs → 1 weight vector) and the evolution method is extremely simple (random bias increments).
- There is no rigorous training algorithm, no saved checkpoints, and no hyperparameter tuning — the project is meant for learning and experimentation.

Quick overview of the code
- main.py
  - Program entry point. Initializes Pygame and runs the generation loop.
  - Creates a population, generates tubes, steps the simulation, and displays the current best agent.
- bird_maker.py
  - bird class: represents an agent with a Pygame surface, position, score tracking, and a brain instance.
  - bird_maker: factory used to create birds.
- brain.py
  - brain class: a minimal neural unit storing weights and computing a tanh activation over a linear combination of four inputs.
  - decision(by, tx, tl, tu) → tanh([by,tx,tl,tu] · weights)
- population.py
  - population class: manages the pool of birds, cloning, mutating (differentiating), running decisions, checking collisions, and choosing the best bird.
- tube_maker.py
  - Simple tube generator that creates top and bottom tubes with a gap at a random vertical offset.

How the agent perceives the world (inputs to the brain)
- by: bird's vertical position (rect.centery)
- tx: x coordinate of the nearest tube's center (used by main/population)
- tl: y coordinate of top tube center
- tu: y coordinate of bottom tube center
These four values are concatenated into an input vector and multiplied by the bird's weight vector; the output is passed through tanh. If output > 0 the bird jumps.

How evolution works (very briefly)
- The best bird from the previous generation is cloned into the population.
- Small random bias updates are applied to each bird's weights (update_weights).
- All birds play until they die; their scores are compared and the next generation picks the best bird.
- There are four "axes" (labeled by laxe in the code) used to keep multiple score tracks and vary mutations across generations.

How to run
1. Install dependencies:
   - Python 3.8+
   - pygame
   - numpy
   Example:
   pip install pygame numpy
2. Run:
   python main.py

Notes, limitations and improvement ideas
- Inputs are raw coordinates — consider normalizing inputs (scale to [0,1] or centered around 0) to improve learning stability.
- The brain is just a linear model with tanh. Replace it with a small multi-layer neural network for more expressive behavior.
- Mutation is implemented as random additive biases. Implement crossover, fitness-proportionate selection, and mutations with configurable rates.
- Add checkpointing: save best weights to disk and load them to resume training.
- Improve fitness: currently score increments while bird is alive; consider rewarding distance traveled or successful pass-through-gaps.
- Add more robust collision handling and game reset logic.
- Add visualization for the best bird vs. rest, training curves, and statistics per generation.

Files to start with for changes
- main.py — generation loop and game flow
- brain.py — model and decision function
- population.py — selection, cloning, mutation and scoring
- bird_maker.py — bird state and scoring logic
- tube_maker.py — obstacle creation and movement

License
- The project is published under the GPLv2 as included in the repository.
