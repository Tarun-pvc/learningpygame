import pygame
import os

WIDTH = 1000
HEIGHT = 800
speed = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fight!")

WHITE = (255, 255, 255)
FPS = 60
PLAYER_SIZE = 100

player1 = pygame.image.load(os.path.join('Assets', 'fighter1.png'))
player1_scaled = pygame.transform.scale(player1, (PLAYER_SIZE, PLAYER_SIZE))
player1_left_facing = pygame.transform.flip(player1_scaled, True, False)

player2 = pygame.image.load(os.path.join('Assets', 'fighter2.png'))
player2_scaled = pygame.transform.scale(player2, (PLAYER_SIZE, PLAYER_SIZE))
player2_left_facing = pygame.transform.flip(player2_scaled, True, False)


def draw1(x, y, dirn):

    if dirn == 1:
        WIN.blit(player1_scaled, (x, y))
    else:
        WIN.blit(player1_left_facing, (x, y))
    pygame.display.update()


def draw2(x, y, dirn):

    if dirn == 1:
        WIN.blit(player2_scaled, (x, y))
    else:
        WIN.blit(player2_left_facing, (x, y))
    pygame.display.update()


def moveplayer1(fighterpos, pressed):
    direction = 1
    if pressed[pygame.K_d] and fighterpos.x < WIDTH-PLAYER_SIZE:
        if direction == 1:
            fighterpos.x += speed
        else:
            direction = 1
            fighterpos.x += speed
    if pressed[pygame.K_a] and fighterpos.x >= 0:
        if direction == -1:
            fighterpos.x -= speed
        else:
            direction = -1
            fighterpos.x -= speed

    if pressed[pygame.K_w] and fighterpos.y >= 0:
        fighterpos.y -= speed
    if pressed[pygame.K_s] and fighterpos.y <= HEIGHT-PLAYER_SIZE:
        fighterpos.y += speed

    return direction


def moveplayer12(fighterpos, pressed):
    direction = 1
    if pressed[pygame.K_l] and fighterpos.x < WIDTH-PLAYER_SIZE:
        if direction == 1:
            fighterpos.x += speed
        else:
            direction = 1
            fighterpos.x += speed
    if pressed[pygame.K_j] and fighterpos.x >= 0:
        if direction == -1:
            fighterpos.x -= speed
        else:
            direction = -1
            fighterpos.x -= speed

    if pressed[pygame.K_i] and fighterpos.y >= 0:
        fighterpos.y -= speed
    if pressed[pygame.K_k] and fighterpos.y <= HEIGHT-PLAYER_SIZE:
        fighterpos.y += speed

    return direction


def main():
    # x = 0 This is not a very modular method. It takes up a lot of code lines and looks confusing.
    # y = 0 A better way would be to use pygame.Rect.

    fighterpos1 = pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE)
    fighterpos2 = pygame.Rect(WIDTH-100, HEIGHT-100, PLAYER_SIZE, PLAYER_SIZE)
    Clock = pygame.time.Clock()
    running = True
    while running:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill(WHITE)
        pressed = pygame.key.get_pressed()
        dirn1 = 1
        dirn2 = 1
        dirn1 = moveplayer1(fighterpos1, pressed)
        dirn2 = moveplayer12(fighterpos2, pressed)
        draw1(fighterpos1.x, fighterpos1.y, dirn1)
        draw2(fighterpos2.x, fighterpos2.y, dirn2)

    pygame.quit()


if __name__ == "__main__":
    main()
