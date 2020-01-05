from spinup.utils.test_policy import load_policy, run_policy
import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from MapGenerators.Corners import Corners
from MapGenerators.Pyramid import Pyramid
from MapGenerators.HighPlatform import HighPlatform
from MapGenerators.TwoHighTowers import TwoHighTowers
from Player.Player import Player

_, get_action = load_policy('./spinupPpo')
map = Corners()
player = Player()
env = gym.make("geofriend2-v0", maps=[Basic()], player=player)#Pyramid(), 

for i in range(10):
    o = env.reset()
    env.render()
    d = False
    while not d:
        a = get_action(o)
        o, r, d, _ = env.step(a)
        env.render()