class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """

        move smaller in hopes of finding larger

        """
        max_area = 0

        L, R = 0, len(heights)-1

        while L < R:
            max_area = max(max_area, (R-L) * min(heights[L], heights[R]))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_area







