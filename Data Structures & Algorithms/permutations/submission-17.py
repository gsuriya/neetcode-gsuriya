class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        to avoid slicing, hv boolean array of nums alr used

        """

        res = []

        used = [False] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # choose number (mark as used), pass in remaining
            for i, n in enumerate(nums):
                if used[i]: # if alr used
                    continue

                path.append(n)
                used[i] = True # mark as used
                
                dfs(path)
                
                path.pop()
                used[i] = False

        dfs([])
        return res
        