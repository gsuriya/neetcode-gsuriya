class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        lesson: don't just create random pattern, understand methodology behind pattern 
        and what you want to find

        --------------------------------
        OG array:
        1  2  3  4

        Given one of these, find min:

        4  1  2  3   # rotation = 1  smaller than both

        3  4  1  2   # rotation = 2  greater than both

        2  3  4  1   # rotation = 3  greater than both

        1  2  3  4   # rotation = 0  greater than left, smaller than right
        --------------------------------

        if mid > l, r:
            l = mid+1
        elif mid > l and mid < r:
            r = mid-1
        elif mid < l, r
            return mid # found min

        log(n) --> binary search min val
        """


        """
              R
              M
              L   
        3  4  1  2 
        """

        l, r = 0, len(nums)-1

        while l < r:
            # min binary search
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else: # nums[mid] < nums[r]
                r = mid # theoretically keeping mid in search range b/c mid can be min value
            
        return nums[l]