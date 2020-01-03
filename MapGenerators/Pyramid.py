import random
from MapGenerators.Map import Map
from MapGenerators.MapGenerator import MapGenerator

# Simple map, agents on one side, rewards on the other
from MapGenerators.Obstacle import Obstacle


class Pyramid(MapGenerator):
    def generate(self):
        if random.random() > 0.5:
            map = Map([Obstacle([640, 660], 400, 200)],
                    [[150, 700]],
                    [[random.randint(980, 1180), random.randint(500, 700)]])
        else:
            map = Map([Obstacle([640, 660], 400, 200)],
                    [[1199, 719]],
                    [[random.randint(980, 1180), random.randint(500, 700)]])

        return map


        # [[random.randint(100, 300), random.randint(500, 700)],
        #            [random.randint(440, 840), random.randint(300, 500)],
        #            [random.randint(980, 1180), random.randint(500, 700)]]
