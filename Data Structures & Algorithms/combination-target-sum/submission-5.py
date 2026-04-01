class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        
        dfs(include, i)
        dfs(don't include, i + 1)

        """
            
        res = []

        def dfs(path, path_sum, i):
            # base cases
            if i == len(nums):
                return
            if path_sum == target:
                res.append(path.copy())
                return
            if path_sum > target:
                return
            
            # include, don't move i
            path.append(nums[i])
            path_sum += nums[i]
            dfs(path, path_sum, i)
            path_sum -= nums[i]
            path.pop()

            # dont include, move i
            dfs(path, path_sum, i+1)
        
        dfs([], 0, 0)
        return res


