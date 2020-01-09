from spinup.utils.test_policy import load_policy, run_policy
import gym
import gym_geofriend2

_, get_action = load_policy('./spinupPpo')
env = gym.make("geofriend2-v0")#Pyramid(), 
run_policy(env, get_action, max_ep_len=200)