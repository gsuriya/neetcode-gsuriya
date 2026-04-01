class Solution:
    # optimize for what you'll regret when you're 80 years old on ur deathbed
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack, res = [], [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                c_temp, c_index = stack.pop() # pop number
                res[c_index] = i - c_index # add num in res
            stack.append([t, i])

        return res
        

