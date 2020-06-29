"""Script for launch Brain Games."""
import prompt


def main():
    """Entry point to Brain Games."""
    print('Welcome to the Brain Games!')
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {user}!\n'.format(user=name))


if __name__ == '__main__':
    main()
