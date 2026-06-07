class Solution:
    def hammingWeight(self, n: int) -> int:
        """

        O(# of 1-bits) --> O(1)
        
        use & (n-1) --> removes least significant 1 bit

        """

        count = 0
        while n > 0:
            n &= (n-1)
            count += 1
        return count
    