import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 900))
pygame.display.set_caption("Hellcife Traffic Nightmare")
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(test_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)