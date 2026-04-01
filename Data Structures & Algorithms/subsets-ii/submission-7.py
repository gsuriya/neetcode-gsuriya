class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        if u see the 1 again later, then obv duplicates will occur

        sort --> allows to skip duplicates

        i
        1 1 2

        use it (i+1)
        never use it again (skip all dups)

        """

        res = []

        nums.sort()
        
        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # use it (i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            
            # never use it again
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
            dfs(i)
        
        dfs(0)
        return res

