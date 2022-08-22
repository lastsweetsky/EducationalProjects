SYMBOLS = 'АБВГДЕЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеежзийклмнопрстуфхцчшщъыьэюя 1234567890!@#$%^&*()'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        mode = input('Вы хотите зашифровать или расшифровать текст?\n').lower()
        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите "зашифровать" или "з" для зашифровки или "расшифровать" или "р" для расшифровки.')


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


def main():
    mode = getMode()
    messsage = getMessage()
    key = getKey()
    print('Преобразованый текст:\n'
          f'{getTranslatedMessage(mode, messsage, key)}')


if __name__ == "__main__":
    main()