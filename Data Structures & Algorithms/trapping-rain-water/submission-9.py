class Solution:
    def trap(self, height: List[int]) -> int:
        """

        water for each coord:
            min(maxleft, maxright) - current blocks alr there

        L
                          R
        0 2 0 3 1 0 1 2 3 1  

        maxl = 
        maxr = 

        res = 2
        """

        res = 0 # amount of water blocks

        L, R = 0, len(height)-1
        maxL, maxR = height[L], height[R]
        while L < R: # invariant doesn't make sense at L = R
            if maxL <= maxR:
                res += maxL - height[L+1] if maxL - height[L+1] > 0 else 0
                L += 1
                maxL = max(maxL, height[L])
                
            
            else:
                res += maxR - height[R-1] if maxR - height[R-1] > 0 else 0
                R -= 1
                maxR = max(maxR, height[R])
                
        
        return res






