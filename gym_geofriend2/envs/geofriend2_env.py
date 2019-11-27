import gym
from gym import error, spaces, utils
from gym.utils import seeding

from MapGenerators.Corners import Corners
import pygame
from pygame.locals import *

class GeoFriend2Env(gym.Env):
      """
    Description:
        GeoFriend is the player and his unique and basic objective is to collect all the points that are distributed along the map.
    Observation: 
        Type: Box(2)
        Num	Observation                 Min                  Max
        0	  Circle Position             Left limit           Right limit
        1	  Circle Velocity             -Inf                 Inf
        
    Action:
        Type: Discrete(4)
        Num	Action
        0	Push Circle to the left
        1	Push Circle to the right
        2	Push Circle to the top
        3	Push Circle to the bottom
        
    Reward:
        Reward is 1 if the player collects one point. 
    Starting State:
        All observations are assigned a uniform random value in [-0.05..0.05]
    Episode Termination:
        All the rewards for that map were collected.
    """

  def __init__(self, map, agent=None, screen_res=[640, 400] ):
    self.map = map

    self.action_space = spaces.Discrete(4)
    self.observation_space = spaces.Box(left_limit, right_limit, dtype=np.float32)

    #Init for rendering pygame
    self.screen_res = screen_res
    self.screen, self.gui_window, self.screen_resized = None, None, None

    pygame.init()
    self.screen = pygame.surface.Surface((1280, 800))  # original GF size
    self.screen_resized = pygame.surface.Surface(screen_res)  # original GF size
    pygame.display.set_caption("GeoFriend2")

  # def step(self, action):
  #   ...

  def reset(self):
    self.prepare_frame()

  def render(self, close = False):
    if close:
      pygame.quit()
      self.screen = None
      return

    if self.gui_window is None:
      pygame.init()
      self.screen = pygame.surface.Surface((1280, 800))  # original GF size
      pygame.display.set_caption("GeoFriend2")
      self.gui_window = pygame.display.set_mode(self.screen_res, HWSURFACE | DOUBLEBUF | RESIZABLE)

    self.prepare_frame()

    self.gui_window.blit(pygame.transform.scale(self.screen, self.screen_res), (0, 0))
    pygame.display.flip()

  def prepare_frame(self):
    self.screen.fill((0, 0, 255))
    # Draw obstacles
    for obs in self.map.obstacles:
        pygame.draw.rect(self.screen, (0, 0, 0),
                          [obs.left_x, obs.top_y, obs.right_x - obs.left_x, obs.bot_y - obs.top_y])
    # Draw agents
    if(self.agent):
      agent.render(self.screen)
      agent.step()

    # Draw rewards
    for reward in self.map.rewards:
        pygame.draw.circle(self.screen, (255, 0, 255), [int(reward[0]), int(reward[1])], 25)

  def close(self):
    self.render(close=True)
    return