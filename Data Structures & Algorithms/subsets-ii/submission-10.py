class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # use it (i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            # ~use it (skip dups)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
            dfs(i)
        
        dfs(0)
        return res

        