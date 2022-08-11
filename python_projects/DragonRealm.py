import random
import time

CAVES_NUMBER = (1, 2)


def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
    который готов поделиться с вами своими сокровищами. Во второй —
    жадный и голодный дракон, который мигом вас съест.''')
    print()

def chooseCave():
    chosenCave = ''
    while chosenCave != '1' and chosenCave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        chosenCave = input()

    return chosenCave


def print_with_sleep(message, time_to_sleep = 2):
    print(message)
    time.sleep(time_to_sleep)


def checkCave(chosenCave):
    print_with_sleep('Вы приближаетесь к пещере.')
    print_with_sleep('Топ...\nToп...')
    print_with_sleep('Ее темнота заставляет вас дрожать от страха...')
    print_with_sleep('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()

    friendlyCave = random.randint(CAVES_NUMBER[0], CAVES_NUMBER[1])

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')


playAgain = 'да'
while playAgain == 'да' or playAgain == 'д' or playAgain == 'ls':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input().lower()
else:
    print('Спасибо за игру, друг! Приходи еще.')

