class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """

        Boyer Moore Algorithm

        candidate = 5
        count = 0 (when count = 0, select new candidate)

                i
        5 5 1 1 1 5 5

        """

        candidate = 0
        count = 0
        
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate


