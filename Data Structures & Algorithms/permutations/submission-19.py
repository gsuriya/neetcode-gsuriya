class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            j
        1 2 3
        T F F

                [1, 2, 3]

        """
        
        res = []
       
        # shows indices CURRENTLY used, easy to find "remaining" to permute
        remaining = [False] * len(nums) 

        def dfs(path):
            if sum([1 for val in remaining if val == True]) == len(nums):
                res.append(path.copy())
                return

            for j in range(len(remaining)):
                # already appended this index to path
                if remaining[j] == True:
                    continue

                # use this index
                path.append(nums[j])
                remaining[j] = True
                
                dfs(path)
                
                # backtrack
                path.pop()
                remaining[j] = False
        
        dfs([])
        return res




