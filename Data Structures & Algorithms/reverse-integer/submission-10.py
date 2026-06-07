class Solution:
    def reverse(self, x: int) -> int:
        """

        pop from x and append to res

        """

        INT_MIN = -2**31
        INT_MAX = (2**31) - 1
        signed = 1 if x < 0 else 0
        x = abs(x)
        bound = abs(INT_MIN) if signed else INT_MAX

        res = 0
        while x > 0:
            # pop from x
            digit = x % 10
            x //= 10

            # check if res will go outside integer limit before appending to res
            if res > bound // 10 or (res == bound // 10 and digit > bound % 10):
                return 0

            # append to res
            res = (res * 10) + digit
        
        return res * (-1 if signed else 1)


        