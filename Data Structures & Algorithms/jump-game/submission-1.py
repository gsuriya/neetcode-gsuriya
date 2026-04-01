class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

              i goal
        1 2 0 1 0
        0 1 2 3 4
        """
        
        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal: # >= to cus u can decide to make a smaller jump too directly to the goal
                goal = i # shift goal back
    
        # if goal is index 0, that means can jump to the end from here
        return goal == 0 