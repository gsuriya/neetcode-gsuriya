class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for n in nums:
            if n in seen:
                return True # dups exist

            seen.add(n)
        
        return False