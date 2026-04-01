class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """

        remove the elems = val 
        return # of elems left

        """

        last = len(nums)-1
        
        for i, n in enumerate(nums):
            # if val to remove, then swap with end and pop
            while nums and nums[last] == val:
                nums.pop()
                last -= 1

            if not nums:
                break

            if n == val:
                nums[i], nums[last] = nums[last], nums[i]
                nums.pop() # popping is O(1) removal
                last -= 1
                
        return len(nums)
            