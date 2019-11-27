from gym.spaces import *
import pygame

class Agent():
    def __init__(self, air_movement=False):
        self.a = "a"
        self.x = 30
        self.y = 30

    def step(self, action_circle):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 0),
                           [self.x, self.y],
                           40)