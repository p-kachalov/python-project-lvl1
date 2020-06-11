"""Module for cli functions."""
import prompt


def get_introduction() -> str:
    """
    Request user self introduction.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')

    print('Hello, {user}!'.format(user=name))

    return name
