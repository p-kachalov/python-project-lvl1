"""Script for launch brain progression game."""
from brain_games.games import brain_progression
from brain_games.flow.game import play


def main():
    """Entry point to brain progression game."""
    play(brain_progression)


if __name__ == '__main__':
    main()
