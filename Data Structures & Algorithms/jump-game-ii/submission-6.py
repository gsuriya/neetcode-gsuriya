class Solution:
    def jump(self, nums: List[int]) -> int:
        """

        array window bfs

        R
        L
        2 4 1 1 1 1
        0 1 1 2 2 2

        1. for L-R window, find farthest
        2. create new window, increment level
        - repeat until R >= ednd

        """

        level = 0
        L, R = 0, 0
        
        while R < len(nums)-1:
            # find farthest in window
            farthest_i = 0
            for i in range(L, R+1):
                farthest_i = max(farthest_i, i + nums[i])
            
            # create new window, increment level
            L = R+1
            R = farthest_i
            level += 1

        return level
