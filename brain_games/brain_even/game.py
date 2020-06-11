"""Brain Even game logic."""
from random import randint
from typing import Tuple

from brain_games.scripts import cli

NUMBER_OF_ROUNDS = 3


def get_rules() -> str:
    """
    Return game rules.

    Returns:
        str
    """
    return 'Answer "yes" if number even otherwise answer "no".'


def make_question() -> Tuple[str, str]:
    """
    Generate new question and right answer for even game.

    Returns:
        str: question number
        str: right answer
    """
    number = randint(0, 100)
    answer = 'no' if number % 2 else 'yes'
    return str(number), answer


def start(name: str):
    """
    Start new game.

    Args:
        name: user's name
    """
    won_rounds = 0
    while won_rounds < NUMBER_OF_ROUNDS:
        question, correct_answer = make_question()
        user_answer = cli.get_user_answer(question=question)

        if user_answer != correct_answer:
            cli.report_on_wrong_answer(
                name=name, answer=user_answer, correct_answer=correct_answer,
            )
            return

        cli.report_on_correct_answer()
        won_rounds += 1

    cli.congrats_user_on_win(name=name)
