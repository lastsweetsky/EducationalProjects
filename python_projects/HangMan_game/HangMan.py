import random

from hangman_data import HANGMAN_PICS, ALPHABET, WORD_DICT


def getRandowWord(WORD_DICT):
    wordKey = random.choice(list(WORD_DICT.keys()))
    wordIndex = random.randint(0, len(WORD_DICT[wordKey]) - 1)
    return WORD_DICT[wordKey][wordIndex], wordKey


def displayBoard(missedLetters, correctLetters, secretWord, hangman_pics):
    print(hangman_pics[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
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


def smart_delete_by_indexes(list_to_operate, indexes_to_remove):
    return [element for i, element in enumerate(list_to_operate) if i not in indexes_to_remove]


def choose_difficulty():
    hangman_pics = HANGMAN_PICS.copy()

    difficulty = 'default'
    while difficulty not in 'ЛСТ':
        difficulty = input('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый\n').upper()
    if difficulty == 'С':
        hangman_pics = smart_delete_by_indexes(hangman_pics, [7, 8])

    if difficulty == 'Т':
        hangman_pics = smart_delete_by_indexes(hangman_pics, [3, 5, 7, 8])

    return hangman_pics


def start_game():

    hangman_pics = choose_difficulty()
    missedLetters = ''
    correctLetters = ''
    secretWord, secretSet = getRandowWord(WORD_DICT)
    gameIsDone = False

    return hangman_pics, missedLetters, correctLetters, secretWord, secretSet, gameIsDone


def main():
    print('В И С Е Л И Ц А')

    hangman_pics, missedLetters, correctLetters, secretWord, secretSet, gameIsDone = start_game()

    while True:
        print(f'Секретное слово из набора: {secretSet}')
        displayBoard(missedLetters, correctLetters, secretWord, hangman_pics)

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

            if len(missedLetters) == len(hangman_pics) - 1:
                displayBoard(missedLetters, correctLetters, secretWord, hangman_pics)
                print(f'Вы исчерпали все попытки!\nНе угадано букв:'
                      f' ' + str(len(missedLetters)) + ' и угадано букв: '
                      + str(len(correctLetters)) + f'. Было загадано слово {secretWord}')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                hangman_pics, missedLetters, correctLetters, secretWord, secretSet, gameIsDone = start_game()
            else:
                break


if __name__ == "__main__":
    main()
