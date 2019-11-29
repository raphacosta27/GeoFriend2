# import gym
# env = gym.make('CartPole-v0')
# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
# env.close()

import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from Player.Player import Player
from spinup.utils.test_policy import load_policy, run_policy

map = Basic()
player = Player()
env_fn = lambda : gym.make("geofriend2-v0", map=map, player=player)

_, get_action = load_policy('./spinupPpo')
env = env_fn()


o = env.reset()
env.render()
d = False
while not d:
    a = get_action(o)
    o, r, d, _ = env.step(a)
    env.render()