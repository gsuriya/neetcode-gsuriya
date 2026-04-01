class Solution:
    def jump(self, nums: List[int]) -> int:
        """

            R
          L           
nums    2 4 1 1 1 1
        - --- -----


        """

        # window bfs - number of windows is min val
        res = 0
        L = R = 0
        farthest_i = 0

        while R < len(nums)-1:
            # calculate farthest index to reach from here
            for i in range(L, R+1):
                farthest_i = max(farthest_i, i + nums[i])

            # move L, move R to farthest_i
            L = R+1
            R = farthest_i
            res += 1 # new window created
        
        return res
            



