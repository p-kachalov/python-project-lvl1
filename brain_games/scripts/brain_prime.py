"""Script for launch brain even game."""
from brain_games.games import brain_prime
from brain_games.scripts.brain_games import main


def play():
    """Entry point to brain prime game."""
    main(rules=brain_prime.get_rules(), get_task=brain_prime.get_task)


if __name__ == '__main__':
    play()
