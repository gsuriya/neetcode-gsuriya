class Solution:
    def trap(self, height: List[int]) -> int:
        """

        for each cell
        res += min(maxLeft, maxRight) - height[i]

        moving min --> maxX becomes limiter
        jump to it --> process

        maxL = 2
        maxR = 1

                          R  
          L                
        0 2 0 3 1 0 1 3 2 1
        """

        L, R = 0, len(height)-1
        maxLeft, maxRight = height[0], height[-1]
        res = 0

        while L < R:
            # solve for elem 1 away from L
            if maxLeft < maxRight:
                water_level = maxLeft
                res += water_level - height[L+1] if water_level - height[L+1] >= 0 else 0

                L += 1
                maxLeft = max(maxLeft, height[L])

            # solve for elem 1 away from R
            else:
                water_level = maxRight
                res += water_level - height[R-1] if water_level - height[R-1] >= 0 else 0

                R -= 1
                maxRight = max(maxRight, height[R])
        
        return res



            
        