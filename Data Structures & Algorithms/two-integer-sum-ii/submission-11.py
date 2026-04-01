class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index 1 < index 2
        # w/ binary search: O(nlogn)
        # two pointers: O(n)

        """

        T = 15

              l  r
        1  2  6  9

        if nums[l] + nums[r] > T:
            r -= 1 # go backward
        elif nums[l] + nums[r] < T:
            l += 1 # go forward
        else:
            return [l+1, r+1]
        

        - since the target is GUARENTEED to be reached by two nums, then 
        this method would work even if the array of nums isn't consecutive

        """

        l, r = 0, len(numbers)-1

        while l <= r:
            sum_ = numbers[l] + numbers[r]
            if sum_ > target:
                r -= 1
            elif sum_ < target:
                l += 1
            else:
                return [l+1, r+1]

