import gym
from gym.utils import seeding
from gym.spaces import Discrete, Box

from MapGenerators.Corners import Corners
import pygame
from pygame.locals import *

class GeoFriend2Env(gym.Env):
      """
    Description:
        GeoFriend is the player and his unique and basic objective is to collect all the points that are distributed along the map.
    Observation: 
        Type: Box(2)
        Num	  Observation                     Min                  Max
        0	  Circle Position x             40 (+raio)           1240 (-raio)
        1	  Circle Position y             40 (+raio)           760  (-raio)
        
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

  action_space = Discrete(4)

  def __init__(self):
      self.action_space = Discrete(4)
      self.observation_space = Box(40, right_limit, dtype=np.float32)
      self.GeoFriend2 = None
      
  def render(self):
      if self.GeoFriend2 is not None:
          self.GeoFriend2.render()
                  
  def reset(self):
      self.GeoFriend2 = GeoFriend2()
  
      return self.GeoFriend2.game_state() # nao sei o que retornar ainda

  def step(self, action):
      if self.predict_for is not None:
          return self.tictactoe.board_state.flatten(), 0, True, {}

      translated_action = TicTacToe.translate_position_to_xy(action)
      

      try:
          self.tictactoe.make_move(translated_action[0], translated_action[1])

      except AssertionError:
          return self.tictactoe.board_state.flatten(), -1, True, {}

      reward = 0
      done = False
      winner = self.tictactoe.is_finished()
      if winner == 0:
          move = self._get_random_move()
          self.tictactoe.make_move(move[0], move[1])

          next_winner = self.tictactoe.is_finished()
          if next_winner == 1:
              reward = -1
              done = True
          elif next_winner == 3:
              reward = 0
              done = True

      elif winner == 2:
          reward = 1
          done = True

      elif winner == 3:
          reward = 0
          done = True

      return self.tictactoe.board_state.flatten(), reward, done, {}