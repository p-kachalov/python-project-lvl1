"""Script for launch Brain Games."""
from brain_games.scripts.cli import get_introduction


def main():
    """Entry point to Brain Games."""
    print('Welcome to the Brain Games!')
    get_introduction()


if __name__ == '__main__':
    main()
