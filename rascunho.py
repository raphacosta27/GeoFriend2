import math
def a():
    return 3,5

distance = math.sqrt( ((80-1215)**2)+((80-735)**2) )
print(distance)

python3 load_and_run.py --type A3C --env geofriend2-v0 --actor_path=A3C/models/A3C_ENV_geofriend2-v0_NB_EP_500_BS_64_LR_0.0001_actor.h5 --critic_path=A3C/models/A3C_ENV_geofriend2-v0_NB_EP_500_BS_64_LR_0.0001_critic.h5