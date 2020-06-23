"""Script for launch brain even game."""
from brain_games.flow.game import play
from brain_games.games import brain_even


def main():
    """Entry point to brain even game."""
    play(brain_even)


if __name__ == '__main__':
    main()
