from MapGenerators.Pyramid import Pyramid
from MapGenerators.utils import collision
from Player.Player import Player
import pygame
from pygame.locals import *
import math
import numpy as np
import math

class GeoFriend2:
    def __init__(self, map, player, screen_res=[640, 400]):
        self.map = map.generate()
        self.player = player
        self.player.set_initial_position(self.map.starting_position)
        self.state = None
        self.steps = 0

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
        """Check wether if there are no more rewards in map or if player is out of bounds"""
        player_is_out = False
        playerx, playery = self.player.get_player_position()
        if( (playerx < 80) | (playerx > 1200) | (playery < 80) | (playery > 720) ):
            player_is_out = True
        return (len(self.map.rewards) == 0) | player_is_out

    def get_episode_reward(self, difference):
        playerx, playery = self.player.get_player_position()
        for i in range (0, len(self.map.rewards)):
            rewardx = int(self.map.rewards[i][0])
            rewardy = int(self.map.rewards[i][1])
            distance = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
            if distance <= (self.player.radius + 25):
                del self.map.rewards[i]
                # print("Caught reward")
                return 1000-self.steps
            else:
                if(difference < 0):
                    return 1
                elif (difference > 0):
                    return -1
                else:
                    return 0

    def set_state(self):    
        playerx, playery = self.player.get_player_position()
        state = [playerx, playery]
        for reward in self.map.rewards:
            state.extend([reward[0], reward[1]])
        # distance = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        self.state = np.array(state)
        return self.state

    def player_step(self, action):
        self.steps += 1
        playerx, playery = self.player.get_player_position()
        rewardx = self.map.rewards[0][0]
        rewardy = self.map.rewards[0][1]
        distance_before = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        self.player.player_step(action)
        collided = False
        if(self.check_collide()):
            collided = True

        playerx, playery = self.player.get_player_position()
        distance_after = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        return distance_after-distance_before, collided

    # source: http://www.jeffreythompson.org/collision-detection/circle-rect.php
    def check_collide(self):
        playerx, playery = self.player.get_player_position()
        for obs in self.map.obstacles:
            if( collision(playerx, playery, self.player.radius, obs.center_x - obs.half_width,
                            obs.center_y - obs.half_height, obs.half_width * 2, obs.half_height * 2) ):
                return True
        return False
    
def test():
    map = Pyramid()
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
                    teste.player_step(0)
                elif event.key == pygame.K_RIGHT:
                    teste.player_step(1)
                elif event.key == pygame.K_UP:
                    teste.player_step(2)
                elif event.key == pygame.K_DOWN:
                    teste.player_step(3)
                elif event.key == pygame.K_SPACE:
                    print("Space pressed")
                    # teste.check_reward()    
                    # pxarray = pygame.PixelArray(teste.screen)
                    # pixel = pygame.Color(pxarray[0,0])
                    # print(pixel)
                    print(pygame.surfarray.array3d(teste.screen))
            # if event.type == pygame.MOUSEBUTTONUP:
            #     print("Mouse event")
            #     pos = pygame.mouse.get_pos()
            #     print(pos)

test()