class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

       


        use (i)
        ~use (i+1)
        
        2 5 6 9

        T = 9
        
        """
        res = []

        path = []
        def dfs(i, path_sum):
            if i == len(nums) or path_sum > target: # overshoot
                return
            
            if path_sum == target: # combo found
                res.append(path.copy())
                return
            
            # use, dont move
            path.append(nums[i])
            dfs(i, path_sum + nums[i])

            # ~use, move
            path.pop()
            dfs(i+1, path_sum)
        
        dfs(0, 0)
        return res
           



