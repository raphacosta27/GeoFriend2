import gym
from gym.utils import seeding
from gym.spaces import Discrete, Box

from MapGenerators.Corners import Corners
import pygame
from pygame.locals import *
import numpy as np
from gym_geofriend2.envs.GeoFriend2 import GeoFriend2

class GeoFriend2Env(gym.Env):
    """
    Description:
        GeoFriend is the player and his unique and basic objective is to collect all the points that are distributed along the map.
    Observation: 
        Type: Box(2)
        Num	  Observation                   Min                          Max
        0	  Circle Position x             80 (obstacle+raio)           1200 (1280-obstacle-raio)
        1	  Circle Position y             80 (obstacle+raio)           720  (800-obstacle-raio)
        2     Distance to Reward            65 (raioP + raioR)           1311 (distancia no pior caso, ver caderno)
        ideia2
        2     Reward Position x             65 (obstacle+raio)           1215 (1280-obstacle-raio)
        3     Reward Position y             65 (obstacle+raio)           735  (800-obstacle-raio)
        
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

    def __init__(self, map, player):
        self.action_space = Discrete(4)
        self.observation_space = Box( low = np.array([80,80,65]), 
                                      high = np.array([1200,720,1311]) )
        self.GeoFriend2 = None
        self.map = map
        self.player = player
        
    def render(self, mode='human'):
        if self.GeoFriend2 is not None:
            self.GeoFriend2.render()
                    
    def reset(self):
        self.GeoFriend2 = GeoFriend2(self.map, self.player)
        self.GeoFriend2.reset_view()
        return self.GeoFriend2.set_state() # nao sei o que retornar ainda

    def step(self, action): 
        try:
            difference = self.GeoFriend2.player_step(action)
            print("Difference: ", difference)
        except AssertionError:
            return self.GeoFriend2.state, -1, True, {}

        observation = self.GeoFriend2.set_state()
        reward = self.GeoFriend2.get_episode_reward(difference)
        done = self.GeoFriend2.is_finished()
        return observation, reward, done, {}
