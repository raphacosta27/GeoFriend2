
import gym
import gym_geofriend2
from MapGenerators.Corners import Corners

map = Corners().generate()
env = gym.make('geofriend2-v0', map=map)

env.reset()
while True:
    env.render() 