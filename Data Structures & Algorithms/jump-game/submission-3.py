class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

        move goalpost to the start

              i goal
        1 2 0 1 0


        can i reach the goal? if it can, move goal to i

        """

        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal: # can jump to goalpost
                goal = i
        
        return goal == 0