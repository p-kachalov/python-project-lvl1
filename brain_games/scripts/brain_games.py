"""Script for launch Brain Games."""
from typing import Callable

from brain_games.scripts import cli

NUMBER_OF_ROUNDS = 3


def main(rules: str = None, get_task: Callable[[], dict] = None):
    """
    Entry point to Brain Games.

    Args:
        rules: rules of game
        get_task: function for get new task
    """
    cli.show_welcome_message(rules=rules)
    name = cli.get_introduction()

    if not get_task:
        return

    won_rounds = 0
    while won_rounds < NUMBER_OF_ROUNDS:
        task = get_task()
        user_answer = cli.get_user_answer(question=task['question'])

        if user_answer != task['answer']:
            cli.report_on_wrong_answer(
                name=name, answer=user_answer, correct_answer=task['answer'],
            )
            return

        cli.report_on_correct_answer()
        won_rounds += 1

    cli.congrats_user_on_win(name=name)


if __name__ == '__main__':
    main()
