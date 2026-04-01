class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # add
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            # dont add
            dfs(i+1, path)

        dfs(0, [])
        return res

