
from doctest import BLANKLINE_MARKER
from turtle import screensize
import pygame
import os
pygame.init()
pygame.font.init()

# Constants and Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 10
SPEED = 20
PLAYER_SIZE = 100
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GameBoy Emulator")
SPRITESHEET = pygame.image.load(os.path.join(
    'Assets', 'new_transparent.png')).convert_alpha()

# os.path.join just makes sure that there are no directory issues

WHITE = (255, 255, 255)


def getimage(sprites, width, height, x, y):
    # makes a pygame 'surface' on which we can draw a part of the SPRITESHEET.
    # putting a sprite over the surface we previously made
    image = pygame.Surface((width, height)).convert()
    image.fill(WHITE)  # Without this line, the background is black automatically black. However, if we make the black part transparent, the black parts of the character are also made transparent. >:(
    image.set_colorkey(WHITE)  # makes the White part transparent.

    # (0,0,width,height) is actually the area in which pygame checks for the sprite.
    image.blit(sprites, (0, 0), (x, y, width, height))
    return image


y_unit = 2400/4
x_unit = 1840/4
sprite_sequences = []


def scale(surface):
    retsurf = pygame.transform.scale(surface, (PLAYER_SIZE, PLAYER_SIZE))
    return retsurf


def split():
    x = 0
    y = 0
    sprite_sequence = []
    for i in range(0, 4):
        sprite_sequence = []
        x = 0
        for j in range(0, 4):
            sprite_sequence.append(
                scale(getimage(SPRITESHEET, x_unit, y_unit, x, y)))
            x += x_unit
        sprite_sequences.append(sprite_sequence)
        y += y_unit


split()

BG = pygame.image.load('Assets/Player_House.png')
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

dirn = 1


def checkConditions(playerPos):
    if playerPos.x <= 200 and playerPos.y <= 200:
        return False
    return True


def controls(playerPos, pressed, index):

    global dirn
    if pressed[pygame.K_s] and playerPos.y <= SCREEN_HEIGHT-PLAYER_SIZE-51:
        dirn = 1
        playerPos.y += SPEED
        draw(playerPos, dirn, index)

    # dirn = 2
    elif pressed[pygame.K_d] and playerPos.x < SCREEN_WIDTH-PLAYER_SIZE:
        dirn = 2
        playerPos.x += SPEED
        draw(playerPos, dirn, index)

    # dirn = 3
    elif pressed[pygame.K_a] and playerPos.x >= 0:
        dirn = 3
        playerPos.x -= SPEED
        draw(playerPos, dirn, index)

    # dirn = 4
    elif pressed[pygame.K_w] and playerPos.y >= 55 and checkConditions(playerPos):
        dirn = 4
        playerPos.y -= SPEED
        draw(playerPos, dirn, index)
    else:
        if dirn == 3:
            draw(playerPos, dirn, 0)
        else:
            draw(playerPos, dirn, 1)


def draw(playerPos, dirn, index):
    WIN.blit(BG, (0, 0))
    WIN.blit(sprite_sequences[dirn-1][index], playerPos)
    pygame.display.update()


def check(playerPos):
    if playerPos.x < SCREEN_WIDTH-150 and playerPos.x > SCREEN_WIDTH - 350 and playerPos.y > SCREEN_HEIGHT-200:
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT/4))
        myfont = pygame.font.SysFont('blackadderitc', 50)
        textsurface = myfont.render(
            "You cant go outside! You're in quarantine.", False, (255, 255, 255))
        surface.fill((0, 0, 0))
        surface.blit(textsurface, (0, 0))
        WIN.blit(surface, (0, 0))
        pygame.display.update()


pygame.mixer.init()
music = pygame.mixer.music.load('pallet_town.mp3')
pygame.mixer.music.play(-1)


def main_loop():
    running = True
    clock = pygame.time.Clock()
    playerPos = pygame.Rect(10, 500, PLAYER_SIZE, PLAYER_SIZE)

    index = 0
    while running:
        index = (index+1) % 4
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        controls(playerPos, pressed, index)
        check(playerPos)

    pygame.quit()


if __name__ == "__main__":
    main_loop()
