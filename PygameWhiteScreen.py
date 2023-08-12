import pygame

# Variables
run = True
resolotion = (800, 800)

# initialize pygame
pygame.init()
screen = pygame.display.set_mode(resolotion)
clock = pygame.time.Clock()

# Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(WHITE)
    clock.tick(60)

    pygame.display.flip()

pygame.quit()
