class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        
        i
        1 2 3 3

        seen = []

        --> know a duplicate exists


        """
        seen = []

        for n in nums:
            if n in seen:
                return True # duplicate cus this number was already seen
            
            seen.append(n)
        
        return False



