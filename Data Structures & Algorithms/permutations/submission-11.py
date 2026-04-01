class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(path, remaining):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(remaining)):
                path.append(remaining[i])
                dfs(path, remaining[:i] + remaining[i+1:])
                path.pop()
            

        dfs([], nums)
        return ans


