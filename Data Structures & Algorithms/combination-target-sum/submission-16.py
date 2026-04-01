class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        repeatedly use the same number, therefore...

        1. use it (i)
        2. ~use it (i+1)

        """
        res = []
        def dfs(i, path, path_sum):
            if path_sum > target or i == len(nums):
                return
            if path_sum == target:
                res.append(path.copy())
                return
            
            # use it
            path.append(nums[i])
            dfs(i, path, path_sum + nums[i])
            # dont use
            path.pop()
            dfs(i+1, path, path_sum)
        
        dfs(0, [], 0)
        return res
            


