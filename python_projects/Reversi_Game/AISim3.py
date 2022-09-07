import random
import sys

WIDTH = 8
HEIGHT = 8


def drawBoard(board):
    print(' 12345678\n'
          ' +-------+')
    for y in range(HEIGHT):
        print(y + 1, end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print(y + 1)
    print(' +-------+\n'
          ' 12345678')


def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board


def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:

            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:

                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1


def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy


def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def enterPlayerTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Вы играете за X или O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy


def isOnCorner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Укажите ход, текст "выход" для завершения игры или "подсказка" для вывода подсказки.')
        move = input().lower()
        if move == 'выход' or move == 'подсказка':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Это недопустимый ход. Введите номер столбца (1-8) и номер ряда (1-8).')
            print('К примеру, значение 81 перемещает в верхний правый угол.')

    return [x, y]


def getCornerBestMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def getWorstMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves)

    worstScore = 64
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, tile, x, y)
        score = getScoreOfBoard(boardCopy)[tile]
        if score < worstScore:
            worstMove = [x, y]
            worstScore = score

    return worstMove


def getRandomMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    return random.choice(possibleMoves)


def isOnSide(x, y):
    return x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1


def getCornerSideBestMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    for x, y in possibleMoves:
        if isOnSide(x, y):
            return [x, y]

    return getCornerBestMove(board, tile)


def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print(f'Ваш счет: {scores[playerTile]}. Счет компьютера: {scores[computerTile]}.')


def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()

    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == 'Человек':
            if playerValidMoves != []:
                move = getCornerBestMove(board, computerTile)
                makeMove(board, playerTile, move[0], move[1])
            turn = 'Компьютер'

        elif turn == 'Компьютер':
            if computerValidMoves != []:
                move = getWorstMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'Человек'


NUM_GAMES = 250
xWins = oWins = ties = 0

print('Приветствуем в игре "Реверси"!')

playerTile, computerTile = ['X', 'O']

for i in range(NUM_GAMES):
    finalBoard = playGame(playerTile, computerTile)

    scores = getScoreOfBoard(finalBoard)
    print(f'{i + 1}: X набрал {scores["X"]} очков. О набрал {scores["O"]} очков.')
    if scores[playerTile] > scores[computerTile]:
        xWins += 1
    elif scores[playerTile] < scores[computerTile]:
        oWins += 1
    else:
        ties += 1

print(f'Number of X wins: {xWins} {xWins / NUM_GAMES * 100}%')
print(f'Number of O wins: {oWins} {oWins / NUM_GAMES * 100}%')
print(f'Number of defeats: {ties} {ties / NUM_GAMES * 100}%')
