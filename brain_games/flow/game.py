"""Common game logic."""
from brain_games.flow import cli

NUMBER_OF_ROUNDS = 3


def play(game):
    """
    Game flow.

    Args:
        game: game to play
    """
    name = cli.greeting_user(game_rules=game.DESCRIPTION)

    won_rounds = 0
    while won_rounds < NUMBER_OF_ROUNDS:
        question, correct_answer = game.get_task()
        user_answer = cli.get_user_answer(question=question)

        if user_answer != correct_answer:
            cli.report_on_wrong_answer(
                name=name, answer=user_answer, correct_answer=correct_answer,
            )
            return

        cli.report_on_correct_answer()
        won_rounds += 1

    cli.congrats_user_on_win(name=name)
