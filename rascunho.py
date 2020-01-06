import math
def a():
    return 3,5

distance = math.sqrt( ((80-1215)**2)+((80-735)**2) )
print(distance)



try:
    difference, collided = self.GeoFriend2.player_step(action)
except AssertionError:
    return self.GeoFriend2.state, -1, True, {}

if collided:
    return self.GeoFriend2.state, -1, True, {}
else:
    observation = self.GeoFriend2.set_state()
    reward = self.GeoFriend2.get_episode_reward(difference, collided)
    done = self.GeoFriend2.is_finished()
    return observation, reward, done, {}