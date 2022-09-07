import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TEXT_COLOR = (0,0,0)
BACKGROUND_COLOR = (255,255,255)
FPS = 60
BADDIE_MIN_SIZE = 10
BADDIE_MAX_SIZE = 40
BADDIE_MIN_SPEED = 1
BADDIE_MAX_SPEED = 8
ADD_NEW_BADDIE_RATE = 6
PLAYER_MOVE_RATE = 5


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXT_COLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),
                                        pygame.FULLSCREEN)
pygame.display.set_caption('DooooDGER')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 35)

gameOverSound = pygame.mixer.Sound('game_lost.mp3')
pygame.mixer.music.load('background.mp3')

playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
playerRect = playerStretchedImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

windowSurface.fill(BACKGROUND_COLOR)
drawText('DoDgEr', font, windowSurface, (WINDOW_WIDTH/3), WINDOW_HEIGHT/3)
drawText('Press space to start', font, windowSurface,
         (WINDOW_WIDTH/5)-30, (WINDOW_HEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0

while True:
    baddies = []
    score = 0
    playerRect.topleft = (WINDOW_WIDTH/2, WINDOW_HEIGHT-50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True

                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0

                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]

        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADD_NEW_BADDIE_RATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIE_MIN_SIZE, BADDIE_MAX_SIZE)
            newBaddie = {'rect':pygame.Rect(random.randint(0, WINDOW_WIDTH - baddieSize),
                                            0-baddieSize, baddieSize, baddieSize),
                         'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                         'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize)), }

            baddies.append(newBaddie)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYER_MOVE_RATE, 0)
        if moveRight and playerRect.right < WINDOW_WIDTH:
            playerRect.move_ip(PLAYER_MOVE_RATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYER_MOVE_RATE)
        if moveDown and playerRect.bottom < WINDOW_HEIGHT:
            playerRect.move_ip(0< PLAYER_MOVE_RATE)

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in baddies[:]:
            if b['rect'].top > WINDOW_HEIGHT:
                baddies.remove(b)

        windowSurface.fill(BACKGROUND_COLOR)
        drawText(f'Score {score}', font, windowSurface, 10, 0)
        drawText(f'Top score {topScore}', font, windowSurface, 10, 40)
        windowSurface.blit(playerStretchedImage, playerRect)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

    pygame.mixer.music.stop()
    gameOverSound.play()
    drawText('Game Over', font, windowSurface, (WINDOW_WIDTH/3), (WINDOW_HEIGHT/3))
    drawText('Press any key to start new game', font, windowSurface,
             (WINDOW_WIDTH/3)-120, (WINDOW_HEIGHT/3)+50)
    pygame.display.update()
    waitForPlayerToPressKey()
    gameOverSound.stop()