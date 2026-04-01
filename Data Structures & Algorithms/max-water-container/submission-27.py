class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """

        shortest one is the limiter, so move shorter in hopes of finding taller

        """
        
        L, R = 0, len(heights)-1
        max_area = 0

        while L < R:
            max_area = max(max_area, (R-L) * min(heights[L], heights[R]))
            
            # move shorter in hopes of finding taller bar
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        
        return max_area







