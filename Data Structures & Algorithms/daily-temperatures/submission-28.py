class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        monotonic decreasing stack

        once popped from stack --> you can "solve" it

            i
        30 38 30 36 35 40 28

        stack = [
        ]

        """ 

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # pop and solve
                pt, pi = stack.pop()
                res[pi] = i - pi

            stack.append((t, i))
        
        return res