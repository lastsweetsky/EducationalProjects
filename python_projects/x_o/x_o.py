from python_projects.x_o.utils import *


def main():
    print('Игра "Крестики-нолики"')

    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print(f'{turn} ходит первым')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Человек':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Поздравляем! Вы выиграли!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Ничья!')
                        break
                    else:
                        turn = 'Компьютер'

            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('Компьютер победил! Вы проиграли!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('Ничья!')
                        break
                    else:
                        turn = 'Человек'

        print('Сыграем еще раз? (да или нет)')
        if not input().lower().startswith(('д','l')):
            break


if __name__ == "__main__":
    main()