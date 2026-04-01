class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        # if complement in prev_map, return those indices
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prev_map:
                return [prev_map[complement], i]

            prev_map[n] = i

        return []
        
        