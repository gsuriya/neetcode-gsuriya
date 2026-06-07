class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        XOR same # yields 0 --> all bits r the same

        7 ^ 6 ^ 6 ^ 7 ^ 8
        7 ^ 7 ^ 6 ^ 6 ^ 8 (commutative property)
        0 ^ 0 ^ 8 --> 8

        """

        res = 0
        for n in nums:
            res ^= n
        return res