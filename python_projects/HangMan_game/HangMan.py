import random

from hangman_data import HANGMAN_PICS, ALPHABET, WORD_LIST


def getRandowWord(WORD_LIST):
    wordIndex = random.randint(0, len(WORD_LIST) - 1)
    return WORD_LIST[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        guess = input('Введите букву.\n').lower()
        if len(guess) != 1:
            print('Пожалуйста введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже назвали эту букву. Назовите дргую.')
        elif guess not in ALPHABET:
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def playAgain():
    return input('Хотите сыграть еще? (да или нет)\n').lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandowWord(WORD_LIST)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print(f'ДА! Секретное слово - "{secretWord}"! Вы угадали!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess


        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'Вы исчерпали все попытки!\nНе угадано букв:'
              f' ' + str(len(missedLetters)) + ' и угадано букв: '
              + str(len(correctLetters)) + f'. Было загадано слово {secretWord}')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandowWord(WORD_LIST)
        else:
            break

