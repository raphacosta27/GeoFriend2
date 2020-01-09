from gym.spaces import *
import pygame
import random
import math
from MapGenerators.utils import collision

class Player():
    def __init__(self):
        self.radius = 40
        self.x = None
        self.y = None
        self.speed = 10
        self.isJump = 0
        self.v = 8
        self.gravity = 0.03
        self.jumpVel = 100
        
    def player_step(self, action, obstacles):
        col = []
        for obs in obstacles:
            isCol, xEgde, yEdge = collision(self.x, self.y, self.radius, 
                    obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                    obs.half_width * 2, obs.half_height * 2)
            if(isCol):
                if(xEgde):
                    col.append(xEgde)
                if(yEdge):
                    col.append(yEdge)
        if action == 0: # Move to the bottom
            if("bottom" not in col):
                self.y += self.speed
        elif action == 1: # Move to the top
            if("top" not in col):
                self.jump()
        elif action == 2: # Move to the Left
            if("left" not in col):
                self.moveLeft()
        elif action == 3: # Move to the Right
            if("right" not in col):
                self.moveRight()
        else:
            raise NameError("Invalid action {0} taken".format(action))
        # Ver se pegou reward
    
    def moveRight(self):
        self.x += self.speed

    def moveLeft(self):
        self.x -= self.speed
    
    def jump(self):
        if self.y > (self.jumpVel + 40 + self.radius): #100 + obstacle + radius
            self.y -= self.jumpVel
        else:
            self.y = 80
        self.isJump = 1
        self.v = 8
    
    def update(self, grounds):
        onGround = False
        for obs in grounds:
            if( (collision(self.x, self.y, self.radius, 
                    obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                    obs.half_width * 2, obs.half_height * 2)[0])):
                onGround = True
        if(onGround == False):
            self.v -= self.gravity
            self.y += self.v
        

                        

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 0),
                           [self.x, self.y],
                           self.radius)
    
    def get_player_position(self):
        return self.x, self.y
    
    def set_initial_position(self, starting_position):
        self.x, self.y = starting_position
    
    def set_position(self, x, y):
        self.x = x
        self.y = y