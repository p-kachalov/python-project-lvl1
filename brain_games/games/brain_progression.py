"""Brain progression game logic."""
import random

PROGRESSIONN_LEN = 10
MIN_STEP = 1
MAX_STEP = 10


def get_rules() -> str:
    """
    Return game rules.

    Returns:
        str
    """
    return 'What number is missing in the progression?'


def get_task() -> dict:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    start = random.randint(MIN_STEP, PROGRESSIONN_LEN)  # noqa: S311
    step = random.randint(MIN_STEP, MAX_STEP)  # noqa: S311
    index = random.randint(0, PROGRESSIONN_LEN)  # noqa: S311

    progression = [num * step for num in range(start, start+PROGRESSIONN_LEN)]
    hide_number = progression[index]
    progression[index] = '...'

    question = '{progression}'.format(
        progression=progression,
    )

    answer = str(hide_number)

    return {'question': question, 'answer': answer}
