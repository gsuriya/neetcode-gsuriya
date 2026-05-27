class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        my way

        for each num
        - choose it, pass in remaining
        - once path is len(nums) --> add to res

        """

        res = []
        def dfs(path, remaining):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            # choose num, pass in remaining
            for i, n in enumerate(remaining):
                path.append(n)
                dfs(path, remaining[:i]+remaining[i+1:])
                path.pop()

        dfs([], nums[:])
        return res

