import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
MOVE_SPEED = 6

windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

WHITE = (255, 255, 255)

player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('cherry.png')
foodStrechedImage = pygame.transform.scale(foodImage, (40, 40))

foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH-20),
                             random.randint(0, WINDOW_HEIGHT-20),
                             20, 20))

foodCounter = 0
NEW_FOOD = 40

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

pickUpSound = pygame.mixer.Sound('pickup.mp3')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
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
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False

            if event.key == K_x:
                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                player.left = random.randint(0, WINDOW_WIDTH - player.width)

            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1],
                                     20, 20))

    foodCounter += 1

    if foodCounter >= NEW_FOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - 20),
                                 random.randint(0, WINDOW_HEIGHT - 20),
                                 20, 20))

    windowSurface.fill(WHITE)

    if moveDown and player.bottom < WINDOW_HEIGHT:
        player.top += MOVE_SPEED
    if moveUp and player.top > 0:
        player.top -= MOVE_SPEED
    if moveLeft and player.left > 0:
        player.left -= MOVE_SPEED
    if moveRight and player.right < WINDOW_WIDTH:
        player.right += MOVE_SPEED

    windowSurface.blit(playerStretchedImage, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top,
                                 player.width + 2, player.height + 2)

            playerStretchedImage = pygame.transform.scale(playerImage,(player.width,
                                                          player.height))
            if musicPlaying:
                pickUpSound.play()

    for food in foods:
        windowSurface.blit(foodStrechedImage, food)

    pygame.display.update()
    mainClock.tick(40)