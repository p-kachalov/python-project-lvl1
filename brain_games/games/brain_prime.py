"""Brain prime game logic."""
import random
from typing import Tuple

MIN_NUMBER = 1
MAX_NUMBER = 100


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """
    Define if number is prime.

    Args:
        number: number to check

    Returns:
        True if number is prime
    """
    if number < 2:
        return False

    for divider in range(2, number):
        if (number % divider) == 0:
            return False

    return True


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311

    question = str(number)

    answer = 'yes' if is_prime(number) else 'no'

    return question, answer
