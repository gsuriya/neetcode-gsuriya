class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Know about complement --> everything else free

        # num --> index; needed so i != j
        nums_map = {}

        for i in range(len(nums)):  # First pass: store num -> index
            nums_map[nums[i]] = i

        for i in range(len(nums)):  # Second pass: find complement
            complement = target - nums[i]

            if complement in nums_map and nums_map[complement] != i:
                return [i, nums_map[complement]]

        return []