class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        find all combinations that sum up to target

        include (i+1)
        dont include (i+1)

        """

        res = []

        def dfs(i, path, path_sum):
            # sum found
            if path_sum == target:
                res.append(path.copy())
                return
            # reached the end
            if i == len(nums):
                return
            # sum too big
            if path_sum > target:
                return
            
            path.append(nums[i])
            dfs(i, path, path_sum + nums[i])
            path.pop()
            dfs(i+1, path, path_sum)
        
        dfs(0, [], 0)
        return res







