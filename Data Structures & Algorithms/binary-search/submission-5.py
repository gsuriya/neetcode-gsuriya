class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
          L              R
        [-1, 0, 2, 4, 6, 8]

        """
        L = 0
        R = len(nums)-1

        return self.binary_search(nums, target, L, R)
       
    def binary_search(self, nums, target, L, R):
        if L > R: # same condition as iterative: while L <= R
            return -1
        
        mid = (L + R) // 2

        if target > nums[mid]:
            return self.binary_search(nums, target, L+1, R)
        elif target < nums[mid]:
            return self.binary_search(nums, target, L, R-1)
        else:
            return mid
        
        


