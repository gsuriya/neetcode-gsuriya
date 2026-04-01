class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """ 
        dynamically update the max area
        """
        l = 0
        r = len(heights) - 1

        # two pointers, move smaller bar in hopes of finding a larger bar
        max_area = 0
        while l < r:
            max_area = max(max_area, (r-l) * min(heights[l], heights[r]))

            # move smaller one
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area