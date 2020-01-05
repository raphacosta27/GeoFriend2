import random
from MapGenerators.Map import Map
from MapGenerators.MapGenerator import MapGenerator
from MapGenerators.utils import collision
import math

# Simple map, agents on one side, rewards on the other
from MapGenerators.Obstacle import Obstacle


class Pyramid(MapGenerator):
    def generate(self):
        obstacles = [Obstacle([640, 660], 400, 200)]  
        
        #check if player position is not colliding with any obstacle
        while True:
            colliding = False
            initial_playerx = random.randint(80, 1200)
            initial_playery = random.randint(80, 720)   
            for obs in obstacles:         
                if( collision(initial_playerx, initial_playery, 40, 
                            obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                            obs.half_width * 2, obs.half_height * 2) ):        
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
                if( (collision(initial_rewardx, initial_rewardy, 25, 
                        obs.center_x - obs.half_width, obs.center_y - obs.half_height, 
                        obs.half_width * 2, obs.half_height * 2))):
                    colliding = True
            if colliding:
                continue
            else:
                break

        map = Map(obstacles,
                [initial_playerx, initial_playery],
                [[initial_rewardx, initial_rewardy]])
        
        return map
