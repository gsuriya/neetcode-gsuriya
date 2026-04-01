class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        """

        choose it (i)
        ~choose it (i+1)

        """

        res = []
        path = []
        path_sum = 0

        def dfs(i, path, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return
            if i == len(nums) or path_sum > target:
                return
            
            path.append(nums[i])
            dfs(i, path, path_sum+nums[i])
            path.pop()
            dfs(i+1, path, path_sum)

        dfs(0, [], 0)
        return res

