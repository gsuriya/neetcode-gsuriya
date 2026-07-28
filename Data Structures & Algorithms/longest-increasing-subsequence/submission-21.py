class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        recursive solution

        dfs(i) = LIS from this i to end of nums

        9 1 4 2 3

        """

        # LIS starting from index i
        cache = {} # i --> LIS from this i to the end
        def dfs(i):
            # last num alw has LIS of 1
            if i == len(nums)-1:
                return 1
            
            if i in cache:
                return cache[i]

            # find valid subsequence starts
            length = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length = max(length, dfs(j))
            
            cache[i] = 1 + length
            return 1 + length

        # return largest LIS out of the indices I can start at
        res = 1
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res


        
