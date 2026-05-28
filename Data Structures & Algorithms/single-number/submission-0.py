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
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
