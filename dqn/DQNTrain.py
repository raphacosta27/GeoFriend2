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

from rl.agents.dqn import DQNAgent, NAFAgent
from rl.policy import BoltzmannQPolicy, LinearAnnealedPolicy, EpsGreedyQPolicy,
from rl.memory import SequentialMemory
from rl.callbacks import Callback, FileLogger

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

def build_model(env, num_actions):
    input = Input(shape=(1,env.observation_space.shape[0]))
    x = Flatten()(input)
    x = Dense(128, activation='relu')(x) #128
    x = Dense(64, activation='relu')(x) #64
    x = Dense(32, activation='relu')(x) #32
    output = Dense(num_actions, activation='linear')(x)
    model = Model(inputs=input, outputs=output)
    print(model.summary())
    memory = SequentialMemory(limit=5000000, window_length=1)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05, nb_steps=10000)
    # policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=num_actions, memory=memory, nb_steps_warmup=100,
                target_model_update=1e-2, policy=policy)
    dqn.compile(Adam(lr=1e-5), metrics=['accuracy', 'mae'])

    return dqn

def build_callbacks(env_name):
    # checkpoint_weights_filename = 'dqn_' + env_name + '_weights_{step}.h5f'
    log_filename = 'dqn_{}_log.json'.format(env_name)
    callbacks = [ModelIntervalCheckpoint(interval=5000)]
    callbacks += [FileLogger(log_filename, interval=100)]
    return callbacks

env = gym.make("geofriend2-v0")
dqn = build_model(env, env.action_space.n)

# callbacks = build_callbacks("GeoFriend2")

dqn.fit(env, nb_steps=500000,
visualize=False,
verbose=1,
callbacks=[ModelIntervalCheckpoint(interval=1000)],
log_interval=1000)

rl.agents.ddpg.DDPGAgent(nb_actions, actor, critic, critic_action_input, 
            memory, gamma=0.99, batch_size=32, nb_steps_warmup_critic=1000, 
            nb_steps_warmup_actor=1000, train_interval=1, memory_interval=1, 
            delta_range=None, delta_clip=inf, random_process=None, custom_model_objects={}, 
            target_model_update=0.001)
