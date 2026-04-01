class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]

        L, R = 0, len(height)-1
        res = 0

        while L < R:
            if maxL < maxR: # maxL is limiter
                L += 1
                res += maxL - height[L] if maxL - height[L] >= 0 else 0
                maxL = max(maxL, height[L])

            else: # maxR is limiter
                R -= 1
                res += maxR - height[R] if maxR - height[R] >= 0 else 0
                maxR = max(maxR, height[R])
        
        return res