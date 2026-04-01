class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """

        T = 3

        L R
        1 2 3 4

        sum = 4 --> R -= 1

        """
        L, R = 0, len(numbers)-1

        while L < R:
            sum_ = numbers[L] + numbers[R]

            # sum smaller, L += 1
            if sum_ < target:
                L += 1
            # sum larger, R -= 1
            elif sum_ > target:
                R -= 1
            # sum equal --> return 1-indexed L & R
            else:
                return [L+1, R+1]
        
        return []