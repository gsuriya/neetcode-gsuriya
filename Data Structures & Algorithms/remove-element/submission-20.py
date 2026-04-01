class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """

        remove the elems = val 
        return # of elems left

        4 3 2

        """

        last = len(nums)-1
        
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                nums.pop() # popping is O(1) removal
                last -= 1
            
            i += 1
                
        return len(nums)



            