import sys


def letter_starter(email):
    name = email.split('@')[0].split('.')[0].capitalize()
    return f'Dear {name}, welcome to our team.  We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(letter_starter(sys.argv[1]))
