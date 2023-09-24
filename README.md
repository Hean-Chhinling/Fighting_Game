# Fighting Game

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-red)](https://www.pygame.org/)
[![SpriteSheet](https://img.shields.io/badge/SpriteSheet-1.3%2B-green)](https://github.com/dr0id/Spritesheet)




https://github.com/Hean-Chhinling/Fighting_Game/assets/92643868/4f3a330d-5124-4f59-9b2b-2a5a81a1c7d3




The Fighting Game is an entertaining two-player combat game with a playful background representation of the University of Debrecen in Hungary. 
Players control characters and engage in battles using simple keyboard inputs. 
The game features movement, jumping, and attacking mechanics.

## Features
- Two players game.
- Player 1 controls:
  - A: Move left
  - D: Move right
  - W: Jump
  - Q or E: Attack
- Player 2 controls:
  - Arrow keys for movement
  - L or P: Attack
- Press the "SPACE" key to pause the game.
- Each player starts with 100 health, and each hit deducts 10 health.
- Attack range determined by a red rectangle created when attacking.

## Installation
1. Clone the repository: `git clone https://github.com/Hean-Chhinling/Fighting_Game.git`
2. Navigate to the project directory: `cd Fighting_Game`
3. Run the game: `python main.py`

## Contributing
I welcome contributions to enhance the game. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`
3. Implement your changes and commit them: `git commit -m "Add new feature"`
4. Push your changes to the branch: `git push origin feature/new-feature`
5. Open a pull request explaining your changes and enhancements.

## Technologies Used
- [Pygame Library](https://www.pygame.org/): Pygame is a popular library for developing 2D games in Python, providing support for graphics, sound, and user input.
- [SpriteSheet](https://github.com/dr0id/Spritesheet): SpriteSheet is a library for handling sprite sheets and displaying animations efficiently.
- Sound effects are downloaded from OpenSource music sound effect online.

## Challenges Faced
The main challenge during the game's development was working with the sprite sheet. 
Accurate identification of each sub-image's dimensions within the sprite sheet was necessary to ensure smooth and consistent animations. 
Failure to do so could lead to incorrect character animations, creating visual inconsistencies during gameplay.

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the following resources for their contributions and inspiration:
- Pygame Documentation
- SpriteSheet Documentation
- OpenSource Music Sound Effects

## Contact
For questions or feedback, feel free to contact me at heanchhinling@gmail.com
