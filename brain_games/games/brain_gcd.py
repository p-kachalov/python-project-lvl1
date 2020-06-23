"""Brain GCD game logic."""
import math
import random

MIN_NUMBER = 1
MAX_NUMBER = 9


RULES = 'Find the greatest common divisor of given numbers.'


def get_task() -> dict:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    multiplier = random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    number1 = multiplier * random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    number2 = multiplier * random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311

    question = '{number1} {number2}'.format(
        number1=number1,
        number2=number2,
    )

    answer = str(math.gcd(number1, number2))

    return {'question': question, 'answer': answer}
