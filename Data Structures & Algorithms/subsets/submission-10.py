class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
     
        either include or don't include

        """

        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        dfs(0, [])
        return res




