"""Module for cli functions."""
import prompt


def show_welcome_message(rules=None):
    """
    Show welcome message and game rules (if it's present).

    Args:
        rules: game rules
    """
    print('Welcome to the Brain Games!')
    if rules:
        print(rules, '\n')


def get_introduction() -> str:
    """
    Request user self introduction.

    Returns:
        str
    """
    name = prompt.string('\nMay I have your name? ')

    print('Hello, {user}!'.format(user=name), '\n')

    return name


def get_user_answer(question: str) -> str:
    """
    Request user answer on question.

    Args:
        question: question to answer

    Returns:
        str
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
