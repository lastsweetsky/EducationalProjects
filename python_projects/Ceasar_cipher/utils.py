SYMBOLS = 'АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрстуфхцчшщъыьэюя 1234567890!@#$%^&*()'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        mode = input('Вы хотите зашифровать, расшифровать или взломать текст?\n').lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки \nили "расшифровать" или "р" для расшифровки \nили "взломать" или "в" для взлома.')


def getMessage():
    print('Введите текст:')
    return input()


def getKey():
    key = 0
    while True:
        key = int(input(f'Введите ключ шифрования (1 - {MAX_KEY_SIZE})' + '\n'))
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated