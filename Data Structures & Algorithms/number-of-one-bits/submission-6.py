class Solution:
    def hammingWeight(self, n: int) -> int:
        """

        & (n-1) --> gets rid of next 1

        """

        count = 0
        while n:
            n &= (n-1)
            count += 1
        
        return count
