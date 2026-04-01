class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # basically two_sum BUT
        # - O(1) space complexity
        # i < j

        # two pointer approach
        # if target too big/small, move l/r

        l, r = 0, len(numbers)-1

        while l <= r:
            sum_ = numbers[l] + numbers[r]

            if sum_ > target:
                r -= 1
            elif sum_ < target:
                l += 1
            else:
                return [l+1, r+1]