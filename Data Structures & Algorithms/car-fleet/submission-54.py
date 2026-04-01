import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

  steps  10 5     3     3        
  speed   1 2     2     1
    pos   x x     x     x
          0 1 2 3 4 5 6 7 8 9 10
                              T

        when steps is decreasing, len(steps) = # of fleets
    
        1. get array of SORTED steps
        2. convert it to decreasing using monotonic stack
        - return len(steps)

        """

        # step 1 - sorted steps  
        steps = []
        for p, s in sorted(zip(position, speed)):
            steps.append((target - p) / s)

        # convert to decreasing monotonic stack
        stack = []
        for s in steps:
            while stack and s >= stack[-1]:
                stack.pop()
            stack.append(s)
        
        return len(stack)
        


            

