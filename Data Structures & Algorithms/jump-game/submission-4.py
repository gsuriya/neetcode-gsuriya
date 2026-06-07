class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

        iterate backwards, move goalpost over to front

              i goal
        1 2 0 1 0

        """

        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0