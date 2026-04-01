class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(1) space, so two pointers
        # Two pointers, measure height at each location

        # Dynamically update max area
        L = 0
        R = len(heights) - 1
        max_area = 0

        while L < R:  # No "=" because one bar can't hold water
            # Calculate area
            curr_area = (R - L) * min(heights[L], heights[R])
            max_area = max(curr_area, max_area)

            # move pointers according to whichver bar is lowest in hopes of finding a larger bar
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return max_area