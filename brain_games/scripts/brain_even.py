"""Script for launch brain even game."""
from brain_games.brain_even import game
from brain_games.scripts.brain_games import main


def play():
    """Entry point to brain even game."""
    game_rules = game.get_rules()
    game_launcher = game.start

    main(game_rules, game_launcher)


if __name__ == '__main__':
    play()
