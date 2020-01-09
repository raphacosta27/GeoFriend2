import gym
from gym.utils import seeding
from gym.spaces import Discrete, Box

import pygame
from pygame.locals import *
import numpy as np
from gym_geofriend2.envs.GeoFriend2 import GeoFriend2
from random import randrange
from Player.Player import Player
from MapGenerators.Pyramid import Pyramid
from MapGenerators.Basic import Basic
from MapGenerators.HighPlatform import HighPlatform

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
    def __init__(self):
        self.action_space = Discrete(4)
        self.maps = [Basic(), Pyramid()] #, HighPlatform()
    
        low =  [80  ,  80, 65  , 65 , 0   ]
        high = [1200, 720, 1215, 735, 1310]

        self.observation_space = Box( low = np.array(low), 
                                      high = np.array(high) ) 

        self.GeoFriend2 = None
        
        self.player = Player()

    def render(self, mode='human'):
        if self.GeoFriend2 is not None:
            self.GeoFriend2.render()
                    
    def reset(self):
        index = randrange(len(self.maps))
        self.GeoFriend2 = GeoFriend2(self.maps[index], self.player)
        self.GeoFriend2.reset_view()
        return self.GeoFriend2.set_state()

    def step(self, action): 
        # print("Action: ", action)
        try:
            difference, collided = self.GeoFriend2.player_step(action)
        except AssertionError:
            return self.GeoFriend2.state, -1, True, {}

        observation = self.GeoFriend2.set_state()
        # print("Observation: ", observation, end="\n")
        reward = self.GeoFriend2.get_episode_reward(difference, collided)
        # print("reward: ", reward)
        done = self.GeoFriend2.is_finished()
        return observation, reward, done, {}
