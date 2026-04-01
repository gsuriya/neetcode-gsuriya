class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        # monotonic increasing stack
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]: # [h, i]
                hp, ip = stack.pop()
                max_area = max(max_area, (i-ip) * hp)
                start = ip

            stack.append([h, start])
        
        # remaining areas
        i = len(heights)
        while stack: # guarenteed h < stack[-1][0]
            hp, ip = stack.pop()
            max_area = max(max_area, (i-ip) * hp)
        
        return max_area
            




        
