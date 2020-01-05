import numpy as np
import gym
import gym_geofriend2
from MapGenerators.Basic import Basic
from Player.Player import Player

from rl.agents import DQNAgent
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import Callback

class ModelIntervalCheckpoint(Callback):
    def __init__(self, interval, verbose=0):
        super(ModelIntervalCheckpoint, self).__init__()
        self.interval = interval
        self.step = 0

        self.rewards = []
        self.last_max = -1

    def reset(self):
        self.rewards = []

    def on_step_begin(self, step, logs):
        if self.step % self.interval == 0:
            if len(self.rewards) > 0:
                mean_reward = np.nanmean(self.rewards, axis=0)
                if mean_reward > self.last_max:
                    filename = 'saved-weights/%s.h5f' % mean_reward
                    print("\nSaving model checkpoint with mean reward %s to %s" % (mean_reward, filename))

                    self.model.save_weights(filename, overwrite=True)

                    self.last_max = mean_reward

            self.reset()

    def on_step_end(self, step, logs={}):

        self.rewards.append(logs['reward'])
        self.step += 1

def build_dqn(env):
    nb_actions = env.action_space.n

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(nb_actions, activation='linear'))

    memory = SequentialMemory(limit=5000000, window_length=1)
    policy = BoltzmannQPolicy()

    dqn = DQNAgent(
        model=model,
        nb_actions=nb_actions,
        memory=memory,
        target_model_update=1e-2,
        policy=policy
    )

    dqn.compile(Adam(lr=1e-5), metrics=['accuracy', 'mae'])

    return dqn

maps = [Basic()]
player = Player()
env = gym.make("geofriend2-v0", maps=[Basic()], player=player)
dqn = build_dqn(env)

log_interval = 10000
dqn.fit(env, nb_steps=5000, visualize=False, verbose=1,
    callbacks=[ModelIntervalCheckpoint(interval=log_interval)],
    log_interval=log_interval
)