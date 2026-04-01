class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the lower bar is the limiter, so move the lower bar in hopes of finding a larger bar

        l, r = 0, len(heights)-1
        max_area = 0

        while l <= r:
            curr_area = (r-l) * min(heights[l], heights[r])
            max_area = max(curr_area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area