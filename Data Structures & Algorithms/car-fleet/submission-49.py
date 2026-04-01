import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

    steps = []


  steps  10 5     3     3        
  speed   1 2     2     1
    pos   x x     x     x
          0 1 2 3 4 5 6 7 8 9 10
                              T

        when steps is decreasing, len(steps) = # of fleets
    
        1. get array of SORTED steps
        2. convert it to increasing using monotonic stack (iterate reverse)
        - return len(steps)

        later cars can merge, so thats y iterate reverse order

        """

        # step 1 - sorted steps  
        steps = []
        for p, s in sorted(zip(position, speed)):
            steps.append((target - p) / s)

        # convert to increasing monotonic stack
        stack = []
        for i in range(len(steps)-1, -1, -1):
            # want to keep the cars in front
            if not stack or steps[i] > stack[-1]:
                stack.append(steps[i])
        return len(stack)







        


            

