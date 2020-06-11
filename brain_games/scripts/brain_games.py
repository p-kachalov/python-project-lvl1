"""Script for launch Brain Games."""
from typing import Callable

from brain_games.scripts import cli


def main(game_rules: str = None, game_launcher: Callable[[str], None] = None):
    """
    Entry point to Brain Games.

    Args:
        game_rules: game rules
        game_launcher: function for starting game
    """
    cli.show_welcome_message(rules=game_rules)
    name = cli.get_introduction()

    if game_launcher:
        game_launcher(name)


if __name__ == '__main__':
    main()
