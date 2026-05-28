class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        x ^ x --> 0

        XORing the same bits will lead to 0s for everything

        x^y^x --> y
        x^x^y
        0^y --> y

        XOR is commutative

        """
        
        res = 0
        for n in nums:
            res ^= n
        return res
