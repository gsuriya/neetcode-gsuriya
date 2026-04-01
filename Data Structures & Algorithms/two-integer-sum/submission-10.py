class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict of vals --> index
        dict_1 = {}
        for i, num in enumerate(nums):
            dict_1[num] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_1 and dict_1[complement] != i:
                return [i, dict_1[complement]]
        
        return []

  
