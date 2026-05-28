class Solution:
    def reverse(self, x: int) -> int:
        """

        reverse using base 10

        before adding next digit, check if it'll overflow
        
        32432
        32439
        overflow conditional:

        if (res > MAX_INT // 10) or 
           (res == MAX_INT // 10 and digit > MAX_INT % 10):
           return 0

        1 2 3 4


        """
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)
        signed = True if x < 0 else False
        bound = abs(MIN_INT) if signed else MAX_INT
        x = abs(x)

        res = 0
        
        while x > 0:
            digit = x % 10 # extract digit
            x //= 10 # chop off digit

            # check that adding to res won't cause overflow
            if (res > bound // 10) or (res == bound // 10 and digit > bound % 10):
                return 0

            res = (res * 10) + digit
        
        return res * (-1 if signed else 1)




