class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        XOR everything the long number will single out

        0 ^ num --> num

        """

        res = 0
        for n in nums:
            res ^= n
        return res