class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        num-1 is NOT in the array

        n = 5

        [2,20,4,10,3,4,5]

        set(2, 20, 4, 10, 3, 5)

        """

        max_count = 0
        nums_set = set(nums)

        for n in nums:
            # if start of sequence --> start counting
            if n-1 not in nums_set:
                curr = 1
                while n+1 in nums_set:
                    curr += 1
                    n += 1
                
                max_count = max(max_count, curr)
        
        return max_count