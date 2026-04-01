class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # recursive
        l = 0
        r = len(nums)-1
        return self.binary_search(nums, target, l, r)
    
    def binary_search(self, nums, target, l , r):
        if l > r: # while l <= r
            return -1
        
        mid = (l+r) // 2

        if target > nums[mid]:
            return self.binary_search(nums, target, mid+1, r)
        elif target < nums[mid]:
            return self.binary_search(nums, target, l, mid-1)
        else: # target == nums[mid]
            return mid
        
