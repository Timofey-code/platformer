## Bot Outrun Simulator!
Welcome to Bot Outrun Simulator, where you have to collect items to build a PC! Traverse 3 levels with different terrain.

BUT... it isn't that easy...

There are 3 AI robots on each level that are programmed to hunt you down at all costs! However, there is 1 extra boomer on level 3, making 4 robots on the hardest level.

There are many types of them - stalkers, sweepers, boomers, shovers, runners... the lists goes on. They each have unique mechanics which makes the game so much more challenging!

Do not worry, for if your system is corrupted, or files deleted by the AIs, you will respawn by being cloned on the same level. 

Are you ready to play? You might want to read further first.

## How to use?

Usable on VS code - make sure you have installed the official Python library, and press the "play" button.

Launch via terminal (python run) - 1. Download or save the code into a file named platformer.py inside your preferred folder.

2. Open your terminal/command prompt and navigate (cd) to that folder.

3. Launch the game by typing:
```bash
python platformer.py
```
(Note: Depending on your system installation, you might need to type python3 platformer.py instead).


## Startup

Before starting, you will need to run an install.
For windows:
```bash
pip install pygame
```

For Mac/Linux:
```bash
pip3 install pygame
```

## Controls
*   **`A`** — Move Left
*   **`D`** — Move Right
*   **`W`** — Jump
*   **`ENTER`** — Start Game / Restart Game after Ultimate Victory
*   **`SPACEBAR`** — Respawn & retry current level after a System Failure (game over)

 ## Mechanics (For Developers)
 **State Matrix Router:** Level transitions dynamically hot-swap platform layouts, item quotas, and AI robot configurations seamlessly without reloading resources.
**AABB Collisions:** Custom axis-aligned bounding box collision routines handle platform grounding, vertical ceiling blocks, and pixel-precise coordinate resets.
**Dynamic Difficulty Scaling:** As you progress to higher levels, enemy jumping thresholds are lowered and boss velocities are adjusted to drastically increase tracking efficiency.
