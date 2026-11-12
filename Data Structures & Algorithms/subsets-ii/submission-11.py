class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        1 2 1

               []
            [1]    []
        [12]  [2] [2] []

          i
        1 1 2

           path=[]
            [1]    []
         [11]  [1]   [1]

        use (i+1)
        ~use (skip all duplicates)

        """

        nums.sort()
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # use (i+1)
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            # ~use (skip all dups)
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, path)


        dfs(0, [])
        return res



