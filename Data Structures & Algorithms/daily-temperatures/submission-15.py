class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        monotonically decreasing

        while temp > top of stack temp:
            - keep popping and "process" result using indicies within stack

        0 0 0 0 0 0 0

        stack = [
            (30, 0)
        ]

        """
        res = [0] * len(temperatures)

        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # process the popped temps and add to res
                popped_t, popped_i = stack.pop()
                res[popped_i] = i - popped_i
        
            stack.append((t, i))
        
        return res
        

            
