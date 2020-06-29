"""Brain GCD game logic."""
import math
import random
from typing import Tuple

MIN_NUMBER = 1
MAX_NUMBER = 9


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    multiplier = random.randint(MIN_NUMBER, MAX_NUMBER)
    number1 = multiplier * random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = multiplier * random.randint(MIN_NUMBER, MAX_NUMBER)

    question = '{number1} {number2}'.format(
        number1=number1,
        number2=number2,
    )

    answer = str(math.gcd(number1, number2))

    return question, answer
