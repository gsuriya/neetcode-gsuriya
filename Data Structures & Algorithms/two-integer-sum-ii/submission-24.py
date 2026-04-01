class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """

        its sorted so 
        - incrementing L increases sum 
        - decrementing R decreases sum

        """
        
        L, R = 0, len(numbers)-1

        while L < R: # index 1 and 2 cannot be equal
            sum_ = numbers[L] + numbers[R]

            if sum_ < target:
                L += 1
            elif sum_ > target:
                R -= 1
            else:
                return [L+1, R+1]
            
        return []