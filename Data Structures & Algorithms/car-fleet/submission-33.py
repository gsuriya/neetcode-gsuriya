import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """ 

        racetrack:  0   1   2   3   4   5   6   7   8   9   10
        speed:      1   2           2           2
        steps:      10  5           3           2
        

        steps:
        1. calculate steps
        2. reverse iterate thru steps
        - increment fleet_count

        """

        # create steps array --> 1. sort by position, 2. create steps
        zipped = list(zip(position, speed))
        zipped.sort()
        steps = []
        for p, s in zipped:
            steps.append((target-p)/s)

        # calc and return fleet count
        fleet_count = 0
        max_steps = 0
        for i in range(len(steps)-1, -1, -1):
            if steps[i] > max_steps:
                max_steps = steps[i]
                fleet_count += 1
        
        return fleet_count




        










        
        