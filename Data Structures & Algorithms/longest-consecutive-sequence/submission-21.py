class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        if n-1 not in nums --> start of seq
        - count how long seq goes from these

        """
        nums_set = set(nums)
        max_length = 0

        for n in nums:
            # start of seq found
            if n-1 not in nums_set:
                count = 1
                while n+1 in nums_set:
                    count += 1
                    n += 1
                max_length = max(max_length, count)
        
        return max_length
