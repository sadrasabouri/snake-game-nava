# Snake Game with Sound (using Nava)

This repository contains a simple implementation of the classic Snake game using Python's built-in `turtle` module. The project is designed to be easy to understand and run, especially for beginners. In the extended version of the game, sound effects are added using the [Nava](https://github.com/openscilab/nava) library, which simplifies audio playback in Python.

## Features

The game includes basic graphical elements using the `turtle` module, keyboard controls to move the snake, and real-time score tracking. The sound-enhanced version also adds background music and effects for game events like food collection and game over. The project is cross-platform and does not depend on any complex graphical or audio subsystems.

## How It Works
The game operates in a continuous loop where it listens for key presses to change the direction of the snake, updates the game screen, checks for collisions, and processes food collection. When the snake collides with the wall or itself, the game resets the snake and score. In the sound-enabled version, background music starts at launch, and additional sounds play when the snake eats food or the game ends. These audio effects are handled with simple `nava.play` calls.

## Requirements

You will need Python 3.x installed on your system. The game uses the `tkinter` module, which is typically bundled with Python. To run the sound version of the game, you also need to install the `nava` library, which handles sound playback.

## Running the Game

To run the basic version without sound, checkout to the `game-without-sound` branch and run the game with:

```bash
python main.py
```

To run the version that includes sound effects, go to the `game-with-sound` folder and run the `main.py` again.

### Sound Credits

All sound effects used in the game are licensed for free use and have been sourced from [Pixabay](https://pixabay.com/). The following contributors provided the sound files:

+ Sound Effect by [Universfield](https://pixabay.com/users/universfield-28281460/)
+ Sound Effect by [Gaston A-P](https://pixabay.com/users/xtremefreddy-32332307/)
+ Sound Effect by [freesound_community](https://pixabay.com/users/freesound_community-46691455/)

