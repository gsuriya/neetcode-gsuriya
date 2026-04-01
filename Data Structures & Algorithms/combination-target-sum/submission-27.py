class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        use it (i)
        ~use it (i+1)

        """
        res = []

        path = []
        def dfs(i, path_sum):
            if i == len(nums) or path_sum > target:
                return
            
            if path_sum == target:
                res.append(path.copy())
                return
            
            # use it (i)
            path.append(nums[i])
            dfs(i, path_sum + nums[i])
            path.pop()

            # ~use it (i+1)
            dfs(i+1, path_sum)
        
        dfs(0, 0)
        return res