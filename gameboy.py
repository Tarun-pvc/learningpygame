import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon!")

spritesheet = pygame.image.load(os.path.join(
    'Assets', 'transparent_spritesheet.png')).convert_alpha()

# os.path.join just makes sure that there are no directory issues


def getimage(sprites, width, height, x, y):
    # makes a pygame 'surface' on which we can draw a part of the spritesheet.
    # putting a sprite over the surface we previously made
    image = pygame.Surface((width, height)).convert_alpha()
    # (0,0,width,height) is actually the area in which pygame checks for the sprite.
    image.blit(sprites, (0, 0), (x, y, width, height))
    return image


sprite_size = 50
# declaring a frame for the sprite. This will be our player.
player = getimage(spritesheet, sprite_size, sprite_size, 0, sprite_size)
playersprites_up = [pygame.transform.scale(getimage(spritesheet, sprite_size, sprite_size, 24, 24), (150, 150)), pygame.transform.scale(
    getimage(spritesheet, sprite_size, sprite_size, 0, 0), (150, 150)), pygame.transform.scale(getimage(spritesheet, sprite_size, sprite_size, sprite_size, 0), (150, 150))]

playersprites_down = [pygame.transform.scale(getimage(spritesheet, sprite_size, sprite_size, sprite_size*2, sprite_size), (150, 150)), pygame.transform.scale(
    getimage(spritesheet, sprite_size, sprite_size, sprite_size*2, 0), (150, 150)), pygame.transform.scale(getimage(spritesheet, sprite_size, sprite_size, 3*sprite_size, 0), (150, 150))]

playersprites_left = [pygame.transform.scale(getimage(spritesheet, 50, 50, 200, 50), (150, 150)), pygame.transform.scale(
    getimage(spritesheet, 50, 50, 200, 0), (150, 150)), pygame.transform.scale(getimage(spritesheet, 50, 50, 250, 0), (150, 150))]

playersprites_right = [pygame.transform.scale(getimage(spritesheet, 50, 50, 300, 50), (150, 150)), pygame.transform.scale(
    getimage(spritesheet, 50, 50, 300, 0), (150, 150)), pygame.transform.scale(getimage(spritesheet, 50, 50, 250, 50), (150, 150))]

BG = pygame.image.load('Assets/Player_House.png')
BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))


def draw():
    WIN.blit(BG, (0, 0))
    WIN.blit(playersprites_up[0], (10, 500))
    pygame.display.update()


def main_loop():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()

    pygame.quit()


if __name__ == "__main__":
    main_loop()
