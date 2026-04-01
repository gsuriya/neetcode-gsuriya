class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        find all combinations that sum up to target

        include (i+1)
        dont include (i+1)

        """

        res = []

        def dfs(i, path, path_sum):
            # record success first
            if path_sum == target:
                res.append(path.copy())
                return
            # out of bounds or overshoot
            if i == len(nums) or path_sum > target:
                return

            # choose nums[i] (allow unlimited use → stay at i)
            path.append(nums[i])
            dfs(i, path, path_sum + nums[i])
            path.pop()

            # skip nums[i] (move to next index)
            dfs(i+1, path, path_sum)

        dfs(0, [], 0)
        return res


