class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        use (i)
        ~use (i+1)

        """

        res = []
        def dfs(i, path, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return
            if i == len(nums) or path_sum > target:
                return
            
            # use (i)
            path.append(nums[i])
            dfs(i, path, path_sum + nums[i])
            path.pop()

            # ~use (i+1)
            dfs(i+1, path, path_sum)
            
        dfs(0, [], 0)
        return res

