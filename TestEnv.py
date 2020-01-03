import gym
import gym_geofriend2

from MapGenerators.Basic import Basic
from MapGenerators.Pyramid import Pyramid
from MapGenerators.HighPlatform import HighPlatform
from Player.Player import Player

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import Callback
from spinup import ppo, sac
import tensorflow as tf

map = Pyramid()
player = Player()
env_fn = lambda : gym.make("geofriend2-v0", maps=[Pyramid(), HighPlatform()], player=player)

# ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)

logger_kwargs = dict(output_dir='spinupSac', exp_name='experiment')

# ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=50, logger_kwargs=logger_kwargs)
sac(env_fn=env_fn, steps_per_epoch=5000, epochs=500, logger_kwargs=logger_kwargs, visualize=True)
# env, test_env = env_fn(), env_fn()
# print(type(env.observation_space.shape[0]))
# print(env.action_space.shape)

# state = env.reset()
# print("State: ", state)
# run = True
# while run:
#     env.render() 