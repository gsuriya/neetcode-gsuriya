class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """

        O(1) space so two pointer approach

        sorted therefore:
        - moving left decreases sum
        - moving right increases sum
        - if sum == target --> return indices

        """

        L, R = 0, len(numbers)-1

        while L < R:
            # calculate sum
            sum_ = numbers[L] + numbers[R]

            # depending on sum, increment pointers or return indices
            if sum_ > target:
                R -= 1
            elif sum_ < target:
                L += 1
            else:
                return [L+1, R+1]
        
        return []






