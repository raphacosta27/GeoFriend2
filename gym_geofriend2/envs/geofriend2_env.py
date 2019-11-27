import gym
from gym import error, spaces, utils
from gym.utils import seeding

from MapGenerators.Corners import Corners
import pygame
from pygame.locals import *

class GeoFriend2Env(gym.Env):

  def __init__(self, map, agents=None, screen_res=[640, 400] ):
    self.agents = agents
    self.map = map

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
    if(self.agents):
      for agent in self.agents:
          agent.render(self.screen)
    # Draw rewards
    for reward in self.map.rewards:
        pygame.draw.circle(self.screen, (255, 0, 255), [int(reward[0]), int(reward[1])], 25)
    
  def close(self):
    self.render(close=True)
    return