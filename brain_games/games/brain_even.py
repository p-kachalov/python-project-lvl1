"""Brain Even game logic."""
from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100


def get_rules() -> str:
    """
    Return game rules.

    Returns:
        str
    """
    return 'Answer "yes" if number even otherwise answer "no".'


def get_task() -> dict:
    """
    Generate new question and right answer for even game.

    Returns:
        dict: dict with question and answer
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    answer = 'no' if number % 2 else 'yes'

    return {'question': str(number), 'answer': answer}
