class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        monotonic decreasing stack

                       i
        30 38 30 36 35 40 28
        1  4  1  2  1  0  0
        0  1  2  3  4  5  6

        stack = [
            (40, 5), (28, 6)
        ]
        
        """
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                pt, pi = stack.pop()
                res[pi] = i - pi 
            
            stack.append((t, i))
        
        return res
        








