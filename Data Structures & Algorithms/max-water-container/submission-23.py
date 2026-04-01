class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        # find max area, update dynamically
        max_area = 0

        while l <= r:
            area = (r-l) * min(heights[l], heights[r]) 
            max_area = max(area, max_area)

            # move pointer in hopes of finding a bigger area
            # move smaller pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_area
        