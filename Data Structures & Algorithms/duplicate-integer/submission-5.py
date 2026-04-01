class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set because LOOK UP IN SET IS O(1)
        nums_set = set()
        for num in nums:
            if num in nums_set: #already added before, adding dup
                return True
            nums_set.add(num)
        return False
         