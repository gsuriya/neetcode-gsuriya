class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        goal: if you pop bars that are in increasing order, 
        there is an easy algo to find max height from those
        - monotonic stack allows you to pop bars that are 
          arranged in increasing order


        """

        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # popping
            edge = i
            while stack and h < stack[-1][0]:
                # max area algo w/ bars in increasing order
                hp, ip = stack.pop()
                edge = ip
                max_area = max(max_area, (i-ip) * hp)
            
            stack.append([h, edge]) # [h, i]

        # stack is increasing now
        i = len(heights)
        while stack:
            hp, ip = stack.pop()
            max_area = max(max_area, (i-ip) * hp)
        
        return max_area

