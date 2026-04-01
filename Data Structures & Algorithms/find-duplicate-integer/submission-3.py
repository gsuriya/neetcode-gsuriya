class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = 4
        # 5 ints within 1-5

        # return int that repeats
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]
        
        return 0
        