from MapGenerators.Basic import Basic
from Player.Player import Player
import pygame
from pygame.locals import *
import math

class GeoFriend2:
    def __init__(self, map, player, screen_res=[640, 400]):
        self.map = map.generate()
        self.player = player
        self.player_points = 0

        #pygame variables
        self.screen_res = screen_res
        pygame.init()
        self.screen = pygame.surface.Surface((1280, 800))  # original GF size
        self.screen_resized = pygame.surface.Surface(screen_res)  # original GF size
        pygame.display.set_caption("GeoFriend2")

    def render(self, close=False):
        #show map
        self.gui_window = pygame.display.set_mode(self.screen_res, HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.prepare_frame()
        self.gui_window.blit(pygame.transform.scale(self.screen, self.screen_res), (0, 0))
        pygame.display.flip()
    
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
    
    def reset(self):
        self.prepare_frame()

    def close(self):
        pygame.quit()
        self.screen = None
        return

    # def is_finished(self):
    def check_reward(self):
        print(len(self.map.rewards))
        # for each reward, check if the distance between the center of the reward and the center of the
        # player is fewer than the sum of both radius
        playerx, playery = self.player.get_player_position()
        for reward in self.map.rewards:
            rewardx = int(reward[0])
            rewardy = int(reward[1])
            distance = math.sqrt( ((playerx-rewardx)**2)+((playery-rewardy)**2) )
            if distance < (self.player.radius + 25):
                print("Caught reward")
            else:
                print("Reward not caught")



    # def make_move(self, x, y):
    #     """ Updates the state with the requested new occupied cell """

map = Basic()
player = Player()
teste = GeoFriend2(map, player)

run = True
teste.reset()
while run:
    teste.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(0)
                print("Moving Left")
            elif event.key == pygame.K_RIGHT:
                player.move(1)
                print("Moving Right")
            elif event.key == pygame.K_UP:
                player.move(2)
                print("Moving up")
            elif event.key == pygame.K_DOWN:
                player.move(3)
                print("Moving down")
            elif event.key == pygame.K_SPACE:
                teste.check_reward()
    