import gym
from gym.utils import seeding
from gym.spaces import Discrete, Box

import pygame
from pygame.locals import *
import numpy as np
from gym_geofriend2.envs.GeoFriend2 import GeoFriend2
from random import randrange

class GeoFriend2Env(gym.Env):
    """
    Description:
        GeoFriend is the player and his unique and basic objective is to collect all the points that are distributed along the map.
    Observation: 
        Type: Box(2)
        Num	  Observation                   Min                          Max
        0	  Circle Position x             80 (obstacle+raio)           1200 (1280-obstacle-raio)
        1	  Circle Position y             80 (obstacle+raio)           720  (800-obstacle-raio)
        
        2     Reward Position x             65 (obstacle+raio)           1215 (1280-obstacle-raio)
        3     Reward Position y             65 (obstacle+raio)           735  (800-obstacle-raio)

        4     Obstacle left_x               25                           1255
        5     Obstacle top_y                25                           775
        6     Obstacle right_X              25                           1255
        7     Obstacle bot_y                25                           775
        .
        .
        .
        .
        
    Action:
        Type: Discrete(4)
        Num	Action
        0	Push Circle to the left
        1	Push Circle to the right
        2	Push Circle to the top
        3	Push Circle to the bottom
        
    Reward:
        Reward is 1 if the player collects one point and 0 if the movement doesnt collect any point. 
    Episode Termination:
        All the rewards for that map were collected.
    """
    # action_space = Discrete(4)
    def __init__(self, maps, player):
        self.action_space = Discrete(4)
        self.maps = maps
        self.map = None
        self.observation_space = None
        self.sort_map()

        self.GeoFriend2 = None
        
        self.player = player

    def sort_map(self):
        index = randrange(len(self.maps))
        self.map = self.maps[index]
        # low = [80,0,65]
        # high = [1200,1310,735]
        low = [0]
        high = [1310]
        # print(self.map.)
        # if(self.map.obstacles):
        #     # for obs in test:
        #     low.extend([25, 25, 25, 25])
        #     high.extend([1255, 775, 1255, 775])

        self.observation_space = Box( low = np.array(low), 
                                      high = np.array(high) )    

    def render(self, mode='human'):
        if self.GeoFriend2 is not None:
            self.GeoFriend2.render()
                    
    def reset(self):
        self.sort_map()
        self.GeoFriend2 = GeoFriend2(self.map, self.player)
        self.GeoFriend2.reset_view()
        return self.GeoFriend2.set_state()

    def step(self, action): 
        try:
            difference = self.GeoFriend2.player_step(action)
        except AssertionError:
            return self.GeoFriend2.state, -1, True, {}

        observation = self.GeoFriend2.set_state()
        # print("Observation: ", observation, end="\n")
        reward = self.GeoFriend2.get_episode_reward(difference)
        done = self.GeoFriend2.is_finished()
        return observation, reward, done, {}
