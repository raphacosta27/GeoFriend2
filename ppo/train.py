import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from MapGenerators.Pyramid import Pyramid
from MapGenerators.HighPlatform import HighPlatform
from MapGenerators.TwoHighTowers import TwoHighTowers
from Player.Player import Player
from spinup import ppo
import tensorflow as tf

env_fn = lambda : gym.make("geofriend2-v0")

# ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)

logger_kwargs = dict(output_dir='spinupPpo', exp_name='experiment')

ppo(env_fn=env_fn, steps_per_epoch=5000, epochs=500, logger_kwargs=logger_kwargs, visualize=False)