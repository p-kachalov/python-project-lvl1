"""Module for cli functions."""
import prompt


def welcome_user():
    """Just meet new user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {user}!'.format(user=name))
