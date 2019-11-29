from MapGenerators.Basic import Basic
from Player.Player import Player
import pygame
from pygame.locals import *
import math
import numpy as np

class GeoFriend2:
    def __init__(self, map, player, screen_res=[640, 400]):
        self.map = map.generate()
        self.player = player
        self.state = None

        #pygame variables
        self.screen_res = screen_res
        pygame.init()
        self.screen = pygame.surface.Surface((1280, 800))  # original GF size
        self.screen_resized = pygame.surface.Surface(screen_res)  # original GF size
        pygame.display.set_caption("GeoFriend2")
    
    def prepare_frame(self):

        self.screen.fill((0, 0, 255))
        # Draw obstacles
        if self.map:
            for obs in self.map.obstacles:
                pygame.draw.rect(self.screen, (0, 0, 0),
                                [obs.left_x, obs.top_y, obs.right_x - obs.left_x, obs.bot_y - obs.top_y])
        #show player
        if self.player:
            self.player.render(self.screen)

        #show rewards
        for reward in self.map.rewards:
            pygame.draw.circle(self.screen, (255, 0, 255), [int(reward[0]), int(reward[1])], 25)    

    def render(self, close = False):
        pygame.init()
        self.screen = pygame.surface.Surface((1280, 800))  # original GF size
        pygame.display.set_caption("GeoFriend2")
        self.gui_window = pygame.display.set_mode(self.screen_res, HWSURFACE | DOUBLEBUF | RESIZABLE)

        self.prepare_frame()

        self.gui_window.blit(pygame.transform.scale(self.screen, self.screen_res), (0, 0))
        pygame.display.flip()
    
    def reset_view(self):
        """ Always come after an init"""
        self.prepare_frame()  

    def close(self):
        pygame.quit()
        self.screen = None
        return

    def is_finished(self):
        return len(self.map.rewards) == 0

    def get_episode_reward(self):
        initial = len(self.map.rewards)
        playerx, playery = self.player.get_player_position()
        for i in range (0, len(self.map.rewards)):
            rewardx = int(self.map.rewards[i][0])
            rewardy = int(self.map.rewards[i][1])
            distance = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
            if distance < (self.player.radius + 25):
                del self.map.rewards[i]       
        if (len(self.map.rewards) < initial):
            print("Caught reward")
            return 1
        else:
            return 0

    def set_state(self, x=None, y=None):    
        playerx, playery = self.player.get_player_position()
        self.state = np.array([playerx, playery])
        return self.state

def test():
    map = Basic()
    player = Player()
    teste = GeoFriend2(map, player)

    run = True
    teste.reset_view()
    while run:
        teste.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.player_step(0)
                    teste.get_reward()
                    print("Moving Left")
                elif event.key == pygame.K_RIGHT:
                    player.player_step(1)
                    teste.get_reward()
                    print("Moving Right")
                elif event.key == pygame.K_UP:
                    player.player_step(2)
                    teste.get_reward()
                    print("Moving up")
                elif event.key == pygame.K_DOWN:
                    player.player_step(3)
                    teste.get_reward()
                    print("Moving down")
                # elif event.key == pygame.K_SPACE:
                #     print("Space pressed")
                #     teste.check_reward()
    