"""Script for launch brain even game."""
from brain_games.games import brain_gcd
from brain_games.flow.game import play


def main():
    """Entry point to brain even game."""
    play(brain_gcd)


if __name__ == '__main__':
    main()
