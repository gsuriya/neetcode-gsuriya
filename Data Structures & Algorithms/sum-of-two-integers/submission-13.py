class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF

        return a if a <= 2**31 -1 else ~(a ^ 0xFFFFFFFF)