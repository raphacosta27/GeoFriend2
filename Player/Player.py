from gym.spaces import *
import pygame

class Player():
    def __init__(self):
        self.radius = 40
        self.x = random.randrange(40 + self.radius, 1240 - self.radius)
        self.y = random.randrange(40 + self.radius, 760 - self.radius) 
        self.vel = 3
        
    def move(self, action):
        if action == 0: # Move to the left
            self.x -= self.vel
        elif action == 1: # Move to the right
            self.x += self.vel
        elif action == 2: # Move to the Top
            self.y += self.vel
        elif action == 3: # Move to the bottom
            self.y -= self.vel
        else:
            raise NameError("Invalid action {0} taken".format(action))

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 0),
                           [self.x, self.y],
                           self.radius)