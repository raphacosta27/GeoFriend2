import random
from MapGenerators.Map import Map
from MapGenerators.MapGenerator import MapGenerator


# Simple map, agents on one side, rewards on the other
class Basic(MapGenerator):

    def generate(self):
        initial_playerx = random.randint(80, 1200)
        initial_playery = random.randint(80, 720)

        initial_rewardx = initial_playerx
        while initial_rewardx == initial_playerx:
            initial_rewardx = random.randint(65, 1215)
        
        initial_rewardy = initial_playery
        while initial_rewardy == initial_playery:
            initial_rewardy = random.randint(65, 735)

        map = Map([],
              [initial_playerx, initial_playery],
              [[initial_rewardx, initial_rewardy]])

        return map
