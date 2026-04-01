class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map: num --> index
        map_nums = {}
        for i in range(len(nums)):
            map_nums[nums[i]] = i
        
        # for each num, check complement in map
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map_nums and map_nums[complement] != i: # the index of this number is not = to the same index
                return [i, map_nums[complement]]  

        
