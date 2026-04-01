class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        start counting from starts of sequences

        """

        max_count = 0
        nums_set = set(nums)

        for n in nums:
            if n-1 not in nums_set: # start of sequence
                count = 1
                while n+1 in nums_set:
                    count += 1
                    n += 1
                max_count = max(max_count, count)

        return max_count
