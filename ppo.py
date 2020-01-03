from spinup.utils.test_policy import load_policy, run_policy
import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from MapGenerators.Corners import Corners
from MapGenerators.Pyramid import Pyramid
from MapGenerators.HighPlatform import HighPlatform
from Player.Player import Player

_, get_action = load_policy('./spinupPpo')
map = Corners()
player = Player()
env = gym.make("geofriend2-v0", maps=[Pyramid(), HighPlatform()], player=player)#
#run_policy(env, get_action, render=False)

for i in range(10):
    o = env.reset()
    env.render()
    d = False
    while not d:
        a = get_action(o)
        o, r, d, _ = env.step(a)
        env.render()