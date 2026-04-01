class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(i, path):
            if i == len(nums):
                ans.append(path.copy())
                return
            
            # include it
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            # don't include it, skip dups
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, path)

        dfs(0, [])
        return ans

