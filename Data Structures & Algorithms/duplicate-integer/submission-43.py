class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """

        seen = []

        --> know a duplicate exists


        "cat"
                 
        [A, B, C, D, E, F, G, H...]

        """
        seen = set()

        for n in nums:
            if n in seen:
                return True # duplicate cus this number was already seen
            
            seen.add(n)
        
        return False



