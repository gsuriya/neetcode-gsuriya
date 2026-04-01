class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # strictly decreasing stack

        # add each number to stack w/ index
        # if num_added > stack[-1], pop the stack and put diff between 
        # the indicies of num_addded and pop() in the array location of pop()

        stack = []
        res = [0 for i in range(len(temperatures))]

        """
        stack = [(38,1)]

        popped = (30,2)
               
                          i  
        temps = [30,38,30,36,35,40,28]    

        res =   [1, 0, 0, 0, 0, 0, 0]


        """
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # check <= case later for dups
                # pop and fill in that index w/ solution
                popped = stack.pop()
                res[popped[1]] = index - popped[1]

            stack.append((temp, index))

        return res

