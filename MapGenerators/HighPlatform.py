import random
from MapGenerators.Map import Map
from MapGenerators.MapGenerator import MapGenerator
from MapGenerators.utils import collision
from MapGenerators.Obstacle import Obstacle
import math


# High platform on one side of the map
class HighPlatform(MapGenerator):
    def __init__(self):
        self.has_obs = True
        
    def generate(self):
        if random.random() > 0.5:
            obstacles = [Obstacle([480, 328], 960, 32)] 
        else:
            obstacles = [Obstacle([800, 328], 960, 32)]
        
        #check if player position is not colliding with any obstacle
        while True:
            colliding = False
            initial_playerx = random.randint(80, 1200)
            initial_playery = random.randint(80, 720)   
            for obs in obstacles:         
                if( collision(initial_playerx, initial_playery, 40, 
                            obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                            obs.half_width * 2, obs.half_height * 2)[0] ):        
                    colliding = True
            if colliding:
                continue
            else:
                break


        # #Do the same for the reward and also check if its not already colliding with player
        while True:
            colliding = False
            initial_rewardx = random.randint(65, 1215) 
            initial_rewardy = random.randint(65, 735)
            distance = math.sqrt( ((initial_playerx-initial_rewardx)**2)+((initial_playery-initial_rewardy)**2) )
            if(distance <= 65):
                continue
            
            for obs in obstacles:         
                if( collision(initial_rewardx, initial_rewardy, 25, 
                        obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                        obs.half_width * 2, obs.half_height * 2)[0]):
                    colliding = True
            if colliding:
                continue
            else:
                break

        map = Map(obstacles,
                [initial_playerx, initial_playery],
                [[initial_rewardx, initial_rewardy]])
        
        return map
