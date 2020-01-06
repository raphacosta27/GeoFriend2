import numpy as np
import gym
import gym_geofriend2
from MapGenerators.Basic import Basic
from Player.Player import Player

from rl.agents import DQNAgent
from keras.models import Sequential
from keras.layers import Input, Dense, Activation, Flatten
from keras.optimizers import Adam
from keras.models import Model

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy, LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import Callback, ModelIntervalCheckpoint, FileLogger

def build_model(env, num_actions):
    input = Input(shape=(1,env.observation_space.shape[0]))
    x = Flatten()(input)
    x = Dense(128, activation='relu')(x) #128
    x = Dense(64, activation='relu')(x) #64
    x = Dense(32, activation='relu')(x) #32
    output = Dense(num_actions, activation='linear')(x)
    model = Model(inputs=input, outputs=output)
    print(model.summary())

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05, nb_steps=10000)
    # policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=num_actions, memory=memory, nb_steps_warmup=100,
                target_model_update=1e-2, policy=policy)
    dqn.compile(Adam(lr=1e-3), metrics=['mae'])

    return dqn


env = gym.make("geofriend2-v0")
dqn = build_model(env, env.action_space.n)

dqn.load_weights("saved-weights/10.653.h5f")

dqn.test(env, nb_episodes=10, visualize=True, verbose=0)