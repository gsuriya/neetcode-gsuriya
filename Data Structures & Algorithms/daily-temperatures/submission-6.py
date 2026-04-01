class Solution:
    # putting the answer in the stack to find the answer for it later
    # on new num, check if its answer to anything in the stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Because we want to know:
	    “When will I see a warmer day?”
        So, we keep track of days that haven’t yet found a warmer temperature.
	    As soon as we find a warmer temperature, we go back and update all the previous colder ones.

        for each num:
            is this num answer to anything in the stack?
            im putting num in the stack, i'll find the answer for num later

        stack = [
            38 37 36 35 34 33 50
        ]

        the 50 that was added is not only the answer for 38, its the answer
        FOR ALL OF THE OTHER NUMBERS AS WELL
        - THAT'S WHAT I WAS MISSING. i thought i couldn't update all the indicies in between

        another example w answers in between and shit:

        stack = [
            39 40
        ]

        by popping num from stack after answer is found for it (basically leads to decreasing stack)
        you can track which ones were updated and not
        monotonically decreasing stack

        you NEVER add to stack all at once
        add GRADUALLY and check as u go
        """

        stack = [
            # [num, index]
        ]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # if i is answer (greater temp) to any previous elems on stack
            # check if num answer to anything on stack
            while stack and t > stack[-1][0]:
                # find diff btwn num and i and update res array
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            # add num to stack to find answer for it later
            stack.append([t, i])
        
        return res


