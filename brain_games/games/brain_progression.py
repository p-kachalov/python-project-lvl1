"""Brain progression game logic."""
import random
from typing import Tuple

PROGRESSIONN_LEN = 10
MIN_STEP = 1
MAX_STEP = 10

DESCRIPTION = 'What number is missing in the progression?'


def make_progression(min_step, max_step, progression_len) -> list:
    """
    Make random arithmetic progression.

    Args:
        min_step: minimal step value
        max_step: maximal step value
        progression_len: length of progression

    Returns:
        a list of numbers an arithmetic progression
    """
    start = random.randint(min_step, max_step)
    step = random.randint(min_step, max_step)

    return [num * step for num in range(start, start+progression_len)]


def get_task() -> Tuple[str, str]:
    """
    Generate new question and right answer for calc game.

    Returns:
        dict: dict with question and answer
    """
    progression = make_progression(
        min_step=MIN_STEP,
        max_step=MAX_STEP,
        progression_len=PROGRESSIONN_LEN,
    )
    index = random.randrange(0, PROGRESSIONN_LEN)
    hide_number = progression[index]
    progression[index] = '...'

    question = '{progression}'.format(
        progression=progression,
    )

    answer = str(hide_number)

    return question, answer
