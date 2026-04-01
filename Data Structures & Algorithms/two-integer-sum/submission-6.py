class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        # convert nums into dict, val --> index
        for i, num in enumerate(nums):
            dict_nums[num] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_nums and dict_nums[complement] != i:
                return [i, dict_nums[complement]]

        return []

  
