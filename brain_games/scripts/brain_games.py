"""Main module of project."""
from brain_games.scripts.cli import welcome_user


def main():
    """Entry point with simple welcome."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
