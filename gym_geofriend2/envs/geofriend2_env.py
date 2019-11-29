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
        Num	  Observation                   Min                     Max
        0	  Circle Position x             40 (+raio=40)           1240 (-raio=40)
        1	  Circle Position y             40 (+raio=40)           760  (-raio=40)
        
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
        self.observation_space = Box( low = np.array([80,80]), 
                                      high = np.array([1200,720]) )
        self.GeoFriend2 = None
        self.map = map
        self.player = player
        
    def render(self):
        if self.GeoFriend2 is not None:
            self.GeoFriend2.render()
                    
    def reset(self):
        self.GeoFriend2 = GeoFriend2(self.map, self.player)
        self.GeoFriend2.reset_view()
        return self.GeoFriend2.set_state() # nao sei o que retornar ainda

    def step(self, action): 
        try:
            self.player.player_step(action)
        except AssertionError:
            return self.GeoFriend2.state, -1, True, {}

        observation = self.GeoFriend2.set_state()
        reward = self.GeoFriend2.get_episode_reward()
        done = self.GeoFriend2.is_finished()
        return observation, reward, done, {}