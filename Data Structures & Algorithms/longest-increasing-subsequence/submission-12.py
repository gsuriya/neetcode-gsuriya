class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        use (i)
        ~use (i+1)

        if not increasing, then prune path and don't dfs

        """

        # returns longest length
        cache = {}
        def dfs(i, prev_i): # prev_i represents last added number
            if (i, prev_i) in cache:
                return cache[(i, prev_i)]
            
            if i == len(nums): # valid subsequence found
                return 0

            # use
            use = 0
            if prev_i == -1 or nums[i] > nums[prev_i]:
                use = 1 + dfs(i+1, i)
            
            # ~use
            skip = dfs(i+1, prev_i)

            cache[(i, prev_i)] = max(use, skip)
            return cache[(i, prev_i)]

        return dfs(0, -1)

