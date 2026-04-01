class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
        
        """
        nums = [3, 4, 7]

        complement = 4

        if 4 is in nums map and the index of this 4 isn't the same index as the 3, then true else false

        nums_map = {
        3   4   7
        |   |   |
        0   1   2  
        } 
        """

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map and nums_map[complement] != i:
                return [i, nums_map[complement]]
        return []



        
        