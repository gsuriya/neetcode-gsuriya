class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """


        L             R
        1 7 2 5 4 7 3 6

        short bar is the limiter 
        --> move the shorter bar in hopes of finding a taller one 

        dynamically update max_area

        """

        max_area = float('-inf')

        L, R = 0, len(heights)-1

        while L < R: # if L and R on same bar, no area for water
            # calculate area and update max
            curr_area = (R-L) * min(heights[L], heights[R])
            max_area = max(max_area, curr_area)

            # move shorter bar in hopes of finding a taller one
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        
        return max_area
