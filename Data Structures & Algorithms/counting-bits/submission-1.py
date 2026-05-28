class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        n = 4

        0 - 0    --> 0 
        1 - 1    --> 1
        2 - 10   --> 1
        3 - 11   --> 2
        4 - 100  --> 1
        5 - 101  --> 2
        6 - 110  --> 2
        7 - 111  --> 3
        8 - 1000 --> 1

        """
        
        res = [0] * (n+1)

        for i in range(n+1):
            # count number of 1 bits in i
            idx = i

            count = 0
            while i > 0:
                i &= (i-1)
                count += 1

            res[idx] = count
        
        return res






