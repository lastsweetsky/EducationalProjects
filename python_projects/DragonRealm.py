import random
import time

CAVES_NUMBERS = (1, 2)
POSSIBLE_YES_ANSWERS = ('lf', 'l', 'yes', 'ye', 'y', 'да', 'д', '1', '2', '+')

def displayIntro():
    print('''\nВы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй —
жадный и голодный дракон, который мигом вас съест.\n''')

def chooseCave():
    chosenCave = ''
    while chosenCave != str(CAVES_NUMBERS[0]) and chosenCave != str(CAVES_NUMBERS[1]):
        chosenCave = input('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)\n')

    return chosenCave


def print_with_sleep(message, time_to_sleep = 2):
    print(message)
    time.sleep(time_to_sleep)


def checkCave(chosenCave):
    print_with_sleep('Вы приближаетесь к пещере.')
    print_with_sleep('Топ...\nToп...')
    print_with_sleep('Ее темнота заставляет вас дрожать от страха...')
    print_with_sleep('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...\n')

    friendlyCave = random.randint(CAVES_NUMBERS[0], CAVES_NUMBERS[1])

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')


playAgain = 'да'

while playAgain in POSSIBLE_YES_ANSWERS:
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    playAgain = input('Попытаете удачу еще раз? (да или нет)\n').lower()
else:
    print('Спасибо за игру, друг! Приходи еще.')

