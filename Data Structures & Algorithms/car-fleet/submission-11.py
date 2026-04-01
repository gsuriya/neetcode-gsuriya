class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # get #iterations to reach to end for each car, create list

        cars = sorted(list(zip(position, speed)))
        iters = [((target - cars[i][0])/cars[i][1]) for i in range(len(cars))]
        stack = []

        for car_i in iters:
            while stack and car_i >= stack[-1]:
                stack.pop()
            stack.append(car_i)
        return len(stack)

        """
        THIS DOES NOT WORK:
        -------------------------------------------
        car_i means #iterations it takes to reach end

        for each car_i:
            while stack and car_i >= stack[-1]:
                stack.pop()
            stack.append(car_i)
        return len(stack) # a monotonically decreasing stack
        -------------------------------------------

        THE REASON WHY:
        (# iterations)

                  (2)             (1)
        racetrack: 1 2 3 4 5 6 7 8 9 10

        so in this example, the code above assumes that
        the 1 above will reach the end FIRST w/o becoming a fleet w/ 2
        HOWEVER, even tho 1 < 2 iterations, if 2 is fast enough, it can catch up

        
        ANOTHER EXAMPLE:
        (speed)
iterations to end: 2         1

                  (8)       (4)  
        racetrack: 1 2 3 4 5 6 7 8 9 10

        here, the car w/ speed = 8 jumps to the 9, and then finishes after another iteration
        again, the code would say these don't count as a fleet

        but the speed=8 is so fast that it catches up even tho takes more iterations
        

        """



        
