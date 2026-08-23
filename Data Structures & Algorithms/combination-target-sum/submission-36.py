class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        generate all unique subsets
        if greater than target --> return

        """

        res = []

        def dfs(i, path, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return

            if i == len(nums) or curr_sum > target:
                return
            
            # include
            path.append(nums[i])
            dfs(i, path, curr_sum + nums[i])
            path.pop()

            # ~include
            dfs(i+1, path, curr_sum)
        
        dfs(0, [], 0)
        return res


