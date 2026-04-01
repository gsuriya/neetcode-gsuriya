class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if u add a number that is already in a set, True duplicates
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else: # num in set
                return True
        return False

