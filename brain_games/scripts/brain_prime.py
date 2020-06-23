"""Script for launch brain even game."""
from brain_games.games import brain_prime
from brain_games.flow.game import play


def main():
    """Entry point to brain prime game."""
    play(brain_prime)


if __name__ == '__main__':
    main()
