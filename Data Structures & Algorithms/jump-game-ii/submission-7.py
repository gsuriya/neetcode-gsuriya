class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        
        min jumps to reach len(nums)-1

          L
            R
        2 4 1 1 1 1

        """

        level = 0
        L, R = 0, 0
        
        while R < len(nums)-1:
            # find how farthest jump is for new window
            farthest = 0
            for i in range(L, R+1):
                farthest = max(farthest, i + nums[i])

            # set pointers at new window
            L = R+1
            R = farthest

            # increment level
            level += 1
        
        return level

