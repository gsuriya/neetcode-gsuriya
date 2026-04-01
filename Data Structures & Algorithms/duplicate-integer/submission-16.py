class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()

        for num in nums:
            if num in empty_set:
                return True
            empty_set.add(num)
        return False