class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed array, O(1) space --> two pointers

        L = 0
        R = len(numbers)-1

        while L < R: # no = b/c don't want sum to be based on off same #
            if numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] > target:
                R -= 1
            else: # numbers[L] == numbers[R]
                return [L+1, R+1]
        
        return []