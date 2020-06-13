"""Script for launch brain even game."""
from brain_games.games import brain_calc
from brain_games.scripts.brain_games import main


def play():
    """Entry point to brain even game."""
    main(rules=brain_calc.get_rules(), get_task=brain_calc.get_task)


if __name__ == '__main__':
    play()
