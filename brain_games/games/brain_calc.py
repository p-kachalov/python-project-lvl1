"""Brain Calc game logic."""
import random
from typing import Tuple

MIN_NUMBER = 0
MAX_NUMBER = 10

DESCRIPTION = 'What is the result of the expression?'


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)  # noqa: S311
    operator = random.choice(['+', '-', '*'])  # noqa: S311

    question = '{number1} {operator} {number2}'.format(
        number1=number1,
        number2=number2,
        operator=operator,
    )

    answer = str(eval(question))  # noqa: S307 WPS421

    return question, answer
