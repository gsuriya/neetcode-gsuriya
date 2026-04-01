class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # check every single L and R pointer brute force

        area = 0
        for L in range(len(heights)):
            for R in range(L+1, len(heights)):
                curr = (R-L) * min(heights[L], heights[R])
                area = max(curr, area)
        
        return area
