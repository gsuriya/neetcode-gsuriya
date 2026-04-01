class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        goal: find the i and j pointer that adds to target
        - such that i < j

        solution: two pointer approach (L and R pointers)

        1. initialize pointers, while loop, ec.
        2. if sum of L and R pointers is > target --> decrement R
           if sum of L and R pointers is < target --> increment L


        time: O(N)
        space: O(1)
        """

        L, R = 0, len(numbers)-1

        while L < R:
            sum_ = numbers[L] + numbers[R]

            if sum_ > target:
                R -= 1
            elif sum_ < target:
                L += 1
            else: # sum == target
                return [L+1, R+1]
        
        return []
        
