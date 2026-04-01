class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_set = set()

        for n in nums:
            # insert each num into set, if num alr in set, then dup exist
            if n not in empty_set:
                empty_set.add(n)
            else:
                return True
        return False

