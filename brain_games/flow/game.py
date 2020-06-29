"""Common game logic."""
import prompt

NUMBER_OF_ROUNDS = 3


def play(game):
    """
    Game flow.

    Args:
        game: game to play
    """
    print('Welcome to the Brain Games!')
    print('{0}\n'.format(game.DESCRIPTION))

    name = prompt.string('\nMay I have your name? ')
    print('Hello, {user}!\n'.format(user=name))

    won_rounds = 0
    while won_rounds < NUMBER_OF_ROUNDS:
        question, correct_answer = game.get_task()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
                user_answer, correct_answer,
            ))
            print("Let's try again, {0}!".format(name))
            return

        print('Correct!')
        won_rounds += 1

    print('Congratulations, {0}!'.format(name))
