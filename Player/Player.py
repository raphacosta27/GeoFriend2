from gym.spaces import *
import pygame
import random
import math

class Player():
    def __init__(self):
        self.radius = 40
        self.x = 1280 - self.radius
        # self.x = 40 + self.radius + 1
        self.y = 800 - 40 - self.radius + 1
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
    
    def set_initial_position(self, starting_position):
        # self.x = 1280 - self.radius - 40 - 1
        self.x, self.y = starting_position
        # self.x = 1280 - 80 - 1
        # self.y = 800 - 80 - 1
    
    def set_position(self, x, y):
        self.x = x
        self.y = y