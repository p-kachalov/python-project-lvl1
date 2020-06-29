"""Brain Calc game logic."""
import operator
import random
from typing import Tuple

MIN_NUMBER = 0
MAX_NUMBER = 10

DESCRIPTION = 'What is the result of the expression?'


def calculate(operand1: int, operand2: int, operator_sign: str) -> int:
    """
    Calculate the result of applying the operation to operands.

    Args:
        operand1: first operand
        operand2: second operand
        operator_sign: operator to apply

    Returns:
        int: result of calculation
    """
    operator_name = {
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
    }

    operator_function = getattr(operator, operator_name[operator_sign])
    return operator_function(operand1, operand2)


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator_sign = random.choice(['+', '-', '*'])

    question = '{number1} {operator} {number2}'.format(
        number1=number1,
        number2=number2,
        operator=operator_sign,
    )

    answer = str(calculate(number1, number2, operator_sign))

    return question, answer
