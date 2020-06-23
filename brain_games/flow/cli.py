"""Functions for interacting with the user."""

import prompt


def greeting_user(game_rules=None) -> str:
    """
    User greetings.

    Show welcome message and game rules (if it's present),
    and request user name.

    Args:
        game_rules: game rules

    Returns:
        str: user name
    """
    print('Welcome to the Brain Games!')
    if game_rules:
        print('{0}\n'.format(game_rules))

    name = prompt.string('\nMay I have your name? ')
    print('Hello, {user}!\n'.format(user=name))

    return name


def get_user_answer(question: str) -> str:
    """
    Request user answer on question.

    Args:
        question: question to answer

    Returns:
        str: user answer
    """
    print(question)
    return prompt.string('Your answer: ')


def report_on_wrong_answer(name: str, answer: str, correct_answer: str):
    """
    Report user about wrong answer.

    Args:
        name: user name
        answer: user answer
        correct_answer: correct answer
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
        answer, correct_answer,
    ))
    print("Let's try again, {0}!".format(name))


def report_on_correct_answer():
    """Report user about correct answer."""
    print('Correct!')


def congrats_user_on_win(name: str):
    """
    Report user about wrong answer.

    Args:
        name: user name
    """
    print('Congratulations, {0}!'.format(name))