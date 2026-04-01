class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        arr numbers increasing order

        O(1) space so probably two pointer approach
         - use fact that its SORTED to our advantage


        L + R < target
        - increase sum --> L += 1

        L + R > target
        - decrease sum --> R -= 1

        L + R == target
        - return [L+1, R+1] (they want 1-indexed answers)

        """

        L, R = 0, len(numbers)-1

        # numbers can't be equal so no L == R
        while L < R:
            sum_ = numbers[L] + numbers[R]

            if sum_ < target:
                L += 1
            elif sum_ > target:
                R -= 1
            else: # == target
                return [L+1, R+1]

        # if no two values found that sum to target
        return [] 

