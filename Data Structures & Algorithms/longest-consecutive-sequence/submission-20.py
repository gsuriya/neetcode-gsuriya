class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        if n-1 not in nums --> start of seq 

        keep counting from start of seq

        """

        nums_set = set(nums)
        max_count = 0

        for n in nums:
            if n-1 not in nums_set: # start of seq
                curr = 1
                while n+1 in nums_set:
                    curr += 1
                    n += 1
                max_count = max(max_count, curr)

        return max_count