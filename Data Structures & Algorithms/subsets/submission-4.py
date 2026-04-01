class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # either add or don't add
        # time: O(n * 2^n) space: O(n)

        subsets = []
        def dfs(i, path):
            if i == len(nums):
                subsets.append(path.copy())
                return

            # add it
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
        
            # dont add it
            dfs(i+1, path)

        dfs(0, [])
        return subsets