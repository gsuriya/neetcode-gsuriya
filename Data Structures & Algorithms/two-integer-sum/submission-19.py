class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}  # int --> index
        for index, num in enumerate(nums):
            nums_map[num] = index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map.keys() and nums_map[complement] != i:
                return [i, nums_map[complement]]

        return []