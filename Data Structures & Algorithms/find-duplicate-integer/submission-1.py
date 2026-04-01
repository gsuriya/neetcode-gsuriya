class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = 4
        # 5 ints within 1-5

        # return int that repeats
        
        empty_set = set()
        for num in nums:
            if num in empty_set: # means we alr added it to set --> duplicate
                return num
            empty_set.add(num)
        
        return 0
        