class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {} # num --> index
        for i in range(len(nums)):
            nums_set[nums[i]] = i 
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_set and nums_set[complement] != i:
                return [i, nums_set[complement]]
        return []
