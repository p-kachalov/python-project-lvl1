"""Script for launch brain progression game."""
from brain_games.games import brain_progression
from brain_games.scripts.brain_games import main


def play():
    """Entry point to brain progression game."""
    main(
        rules=brain_progression.get_rules(),
        get_task=brain_progression.get_task,
    )


if __name__ == '__main__':
    play()
