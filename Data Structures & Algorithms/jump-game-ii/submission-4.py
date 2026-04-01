class Solution:
    def jump(self, nums: List[int]) -> int:
        """

              L
                   R
        2 4 1 1 1 1


        window bfs

        """

        res = 0

        L, R = 0, 0
        while R < len(nums)-1:
            # determine farthest in window
            farthest = 0
            for i in range(L, R+1):
                farthest = max(farthest, nums[i])
            
            # create new window 
            L = R+1
            R += farthest
            res += 1
        
        return res