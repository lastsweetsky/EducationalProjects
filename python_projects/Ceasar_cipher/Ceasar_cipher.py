from python_projects.Ceasar_cipher.utils import *


def main():
    mode = getMode()
    messsage = getMessage()
    if mode[0] != 'в':
        key = getKey()
    print('Преобразованый текст:')
    if mode[0] != 'в':
        print(f'{getTranslatedMessage(mode, messsage, key)}')
    else:
        for key in range(1,MAX_KEY_SIZE +1):
            print(f'{key}. {getTranslatedMessage("расшифровать", messsage, key)}')

if __name__ == "__main__":
    main()