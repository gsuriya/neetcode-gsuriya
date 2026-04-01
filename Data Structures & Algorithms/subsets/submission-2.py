class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # either include or don't include
        # time: O(n * 2^n)
        # space: O(n) - only O(N) because the sublists are part of the result --> remove 2^n sublists from space complexity

        subsets = []
        def dfs(i, path):
            if i == len(nums): # path is completed
                subsets.append(path.copy()) # so path in res doesn't get changed in next recursive changes
                return
            
            # add it
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return subsets

