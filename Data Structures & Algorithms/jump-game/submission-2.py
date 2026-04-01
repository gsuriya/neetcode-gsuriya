class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

              i goal
        1 2 0 1 0

        if jump from this i, can i reach goal?
        - if yes --> goal = i
        - if no --> keep goal where it is

        if goal is at index 0 --> return True else False
        """

        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
            