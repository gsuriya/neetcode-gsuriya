class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. zip the lists
        # 2. create iterations till end list
        # 3. backwards iterate, use stack
        # - if num is > top of stack, add to stack, else dont
        # - return len(stack)

        paired = sorted(list(zip(position, speed)))
        iterations_till_end = [0 for i in range(len(paired))]

        for i in range(len(paired)-1,-1,-1): # (position, speed)
            till_end = target - paired[i][0]
            iterations = till_end / paired[i][1]
            iterations_till_end[i] = iterations
        
        stack = []

        for i in range(len(iterations_till_end)-1, -1, -1):
            if not stack:
                stack.append(iterations_till_end[i])
            elif iterations_till_end[i] > stack[-1]:
                stack.append(iterations_till_end[i])
        
        return len(stack)


        


