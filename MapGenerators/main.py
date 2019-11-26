from Basic import Basic
import pygame
from pygame.locals import *

screen_res=[640, 400]
map = Basic().generate()
pygame.init()
screen = pygame.surface.Surface((1280, 800))  # original GF size
screen_resized = pygame.surface.Surface(screen_res)  # original GF size
pygame.display.set_caption("GeoFriends2")
# gui_window = pygame.display.set_mode(screen_res, HWSURFACE | DOUBLEBUF | RESIZABLE)
# screen.fill((0, 0, 255))
# for obs in map.obstacles:
#     pygame.draw.rect(screen, (0, 0, 0),[obs.left_x, obs.top_y, obs.right_x - obs.left_x, obs.bot_y - obs.top_y])

# gui_window.blit(pygame.transform.scale(screen, screen_res), (0, 0))

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    gui_window = pygame.display.set_mode(screen_res, HWSURFACE | DOUBLEBUF | RESIZABLE)
    screen.fill((0, 0, 255))
    for obs in map.obstacles:
        pygame.draw.rect(screen, (0, 0, 0),[obs.left_x, obs.top_y, obs.right_x - obs.left_x, obs.bot_y - obs.top_y])
    pygame.display.flip()

pygame.quit()