class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """

        use it (i+1)
        ~use it (i+1)

                i
        nums = [1, 2, 3]

            path =      []
              [1]                 []
          [12]      [1]       [2]     []
     [123]  [12] [13] [1]  [23] [2] [3] []

     base case: i == len(nums)

        """
        res = []

        def dfs(i, path):
            # base case: i reaches end of list
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            dfs(i+1, path)
        
        dfs(0, [])
        return res

