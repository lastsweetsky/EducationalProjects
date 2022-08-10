import random

RANGE_OF_NUMBERS = (1, 20)
NUMBER_OF_TRIES = 6


def check_int_input():
    while True:
        try:
            guess = input()
            guess_int = int(guess)
            if RANGE_OF_NUMBERS[0] <= guess_int <= RANGE_OF_NUMBERS[1]:
                return guess_int
            else:
                raise ValueError
        except ValueError:
            print('You entered not a number! Or not in range! Do it again')


def main():
    print('Hi! What is your name,dude?')
    myName = input()

    number = random.randint(RANGE_OF_NUMBERS[0], RANGE_OF_NUMBERS[1])
    print('So, ' + myName + ', i guessing the number from 1 to 20.')

    for guessesTaken in range(NUMBER_OF_TRIES):
        print('Now it\'s your turn to guess! :)')

        guess = check_int_input()

        if guess < number:
            print('Your number is too small! Try again ♥')

        if guess > number:
            print('Your number is too high! Try again ♥')

        if guess == number:
            break

    if guess == number:
        print(f'What a heck?! Good job, {myName}'
              f'! You did it by {guessesTaken + 1} tries!')

    if guess != number:
        print(f'You mad,bro! I guessed {number}.')


if __name__ == '__main__':
    main()
