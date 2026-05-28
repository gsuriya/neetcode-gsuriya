class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # check that each number in range is in nums_set
        for n in range(len(nums)+1):
            if n not in nums_set:
                return n