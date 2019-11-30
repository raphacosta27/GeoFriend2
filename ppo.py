from spinup.utils.test_policy import load_policy, run_policy
import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from Player.Player import Player

_, get_action = load_policy('./spinupPpo')
map = Basic()
player = Player()
env = lambda : gym.make("geofriend2-v0", map=map, player=player)
#run_policy(env, get_action, render=False)

for i in range(1):
    o = env.reset()
    env.render()
    d = False
    while not d:
        a = get_action(o)
        o, r, d, _ = env.step(a)
        env.render()