class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            i
        [30,38,30,36,35,40,28]

        stack = [
            (30, 0)
        ]        

        res = [1, 4, 1, 2, 1, 0, 0]
    
        monotonically decreasing stack


        while t > top of stack:
            keep popping
            "solve" the popped ones
        then append t


        """

        res = [0] * len(temperatures)
        stack = [] # monotonically decreasing stack

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1] 

            stack.append((t, i))
        
        return res







