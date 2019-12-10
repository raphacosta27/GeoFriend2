from MapGenerators.Pyramid import Pyramid
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
        self.player.set_initial_position()
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
                return 1
            else:
                if(difference < 0):
                    return 1
                elif (difference > 0):
                    return -1
                else:
                    return 0

    def set_state(self):    
        playerx, playery = self.player.get_player_position()
        rewardx = self.map.rewards[0][0]
        rewardy = self.map.rewards[0][1]
        # distance = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        state = [playerx, playery, rewardx, rewardy]
        for obs in self.map.obstacles:
                self.state.append(obs.left_x, obs.top_y, obs.right_x, obs.bot_y)

        self.state = np.array(state)
        return self.state

    def player_step(self, action):
        playerx, playery = self.player.get_player_position()
        rewardx = self.map.rewards[0][0]
        rewardy = self.map.rewards[0][1]
        distance_before = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        self.player.player_step(action)
        playerx, playery = self.player.get_player_position()
        print(self.map.obstacles[4])
        print(self.collision( self.map.obstacles[4].left_x, self.map.obstacles[4].top_y, 
                              self.map.obstacles[4].right_x - self.map.obstacles[4].left_x, 
                              self.map.obstacles[4].bot_y - self.map.obstacles[4].top_y,
                              playerx, playery, self.player.radius))
        print("----------------------")
        distance_after = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
        return distance_after-distance_before

    def collision(self, rleft, rtop, width, height,   # rectangle definition
                center_x, center_y, radius):  # circle definition
        """ Detect collision between a rectangle and circle. """

        # complete boundbox of the rectangle
        # rright, rbottom = rleft + width/2, rtop + height/2
        rright, rbottom = rleft + width, rtop + height

        # bounding box of the circle
        cleft, ctop     = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            print("no colission possible")
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if math.hypot(x-center_x, y-center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected
    
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
                    print("Moving Left")
                elif event.key == pygame.K_RIGHT:
                    teste.player_step(1)
                    print("Moving Right")
                elif event.key == pygame.K_UP:
                    teste.player_step(2)
                    print("Moving up")
                elif event.key == pygame.K_DOWN:
                    teste.player_step(3)
                    print("Moving down")
                # elif event.key == pygame.K_SPACE:
                #     print("Space pressed")
                #     teste.check_reward()

test()