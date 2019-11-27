from gym.envs.registration import register

register(
    id='geofriend2-v0',
    entry_point='gym_geofriend2.envs:GeoFriend2Env',
)