import random
import time


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

#TODO: optimize time.sleep for every print in one line
def checkCave(chosenCave):
    print('Вы приближаетесь к пещере.')
    time.sleep(2)
    print('Топ...\nToп...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

#TODO: use random for already known number of caves (made local/global cave_number)
    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

#TODO: add more possible variants of syntaxis (f.e. "ДА", "дА"...)
playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
