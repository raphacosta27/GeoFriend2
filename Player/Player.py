from gym.spaces import *
import pygame
import random

class Player():
    def __init__(self):
        self.radius = 40
        self.x = 40 + self.radius
        self.y = 800 - 40 - self.radius
        self.vel = 10
        
    def player_step(self, action):
        if action == 0: # Move to the left
            self.x -= self.vel
        elif action == 1: # Move to the right
            self.x += self.vel
        elif action == 2: # Move to the Top
            self.y -= self.vel
        elif action == 3: # Move to the bottom
            self.y += self.vel
        else:
            raise NameError("Invalid action {0} taken".format(action))
        # Ver se pegou reward

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 0),
                           [self.x, self.y],
                           self.radius)
    
    def get_player_position(self):
        return self.x, self.y