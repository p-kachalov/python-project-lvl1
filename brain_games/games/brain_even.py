"""Brain Even game logic."""
from random import randint
from typing import Tuple

MIN_NUMBER = 0
MAX_NUMBER = 100


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for even game.

    Returns:
        dict: dict with question and answer
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    question = str(number)
    answer = 'no' if number % 2 else 'yes'

    return question, answer
