from Basic import Basic
import pygame
from pygame.locals import *

map = Basic().generate()
pygame.init()
screen = pygame.display.set_mode((640,400))

run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    # for obs in map.obstacles:
    #     pygame.draw.rect(screen, (0, 0, 0),[obs.left_x, obs.top_y, obs.right_x - obs.left_x, obs.bot_y - obs.top_y])
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

pygame.quit()