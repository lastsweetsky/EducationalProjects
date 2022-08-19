from python_projects.Hot_Cold_Game.data import *
from python_projects.Hot_Cold_Game.utils import *


def main():
    print(f'\nI guess {NUM_DIGITS} digit number that you need to guess.\n'
          'I will give you some clues...\n'
          'When i print:   It\'s mean:\n'
          'Cold:           Any numbers were guessed\n'
          'Warm:           One nuber is guessed, but not the correct position\n'
          'Hot:            One number and its position is guessed\n')

    while True:
        secretNum = getSecretNum()
        print(f'So, I guessed the number. You have {MAX_GUESS} tries to guess it')

        guessTaken = 1
        while guessTaken <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                guess = input(f'\nTry number {guessTaken}\n'
                              'Your number: ')

            print(getClues(guess, secretNum))
            guessTaken += 1

            if guess == secretNum:
                break
            if guessTaken > MAX_GUESS:
                print(f'No more tries left for you. I guessed {secretNum}.')

        print('Do you want to play one more time? (y or n)')
        if not input().lower().startswith(('y','д','l')):
            break

if __name__ == "__main__":
    main()