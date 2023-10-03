import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RABBIT_SIZE = 50
RABBIT_JUMP_SPEED = 12
GRAVITY = 1

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Rabbit Game")

rabbit_img = pygame.image.load("rabbit.png")
rabbit_img = pygame.transform.scale(rabbit_img, (RABBIT_SIZE, RABBIT_SIZE))
rabbit_rect = rabbit_img.get_rect()

rabbit_x = SCREEN_WIDTH // 2 - RABBIT_SIZE // 2
rabbit_y = SCREEN_HEIGHT - RABBIT_SIZE
jumping = False
jump_count = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -RABBIT_JUMP_SPEED:
            neg = 1
            if jump_count < 0:
                neg = -1
            rabbit_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = RABBIT_JUMP_SPEED

    if rabbit_y < SCREEN_HEIGHT - RABBIT_SIZE:
        rabbit_y += GRAVITY

    screen.fill(WHITE)
    screen.blit(rabbit_img, (rabbit_x, rabbit_y))
    pygame.display.update()
    clock.tick(30)
