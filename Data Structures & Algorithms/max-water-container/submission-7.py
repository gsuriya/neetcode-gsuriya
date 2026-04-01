class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1

        area = 0
        while L < R:
            # compute the area of L and R
            curr = (R-L) * min(heights[L], heights[R])
            area = max(area, curr)

            # shift smaller pointer
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return area