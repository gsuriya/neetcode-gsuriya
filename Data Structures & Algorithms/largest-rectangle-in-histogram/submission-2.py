class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                # main algo
                h_popped, i_popped = stack.pop()
                width = i - i_popped
                height = h_popped
                max_area = max(width * height, max_area)
                start = i_popped
            stack.append((h, start))
        
        i = len(heights)
        while stack:
            # same algo
            h_popped, i_popped = stack.pop()
            width = i - i_popped
            height = h_popped
            max_area = max(width * height, max_area)

        return max_area

        """
        STEP 1: heights pass

        for each height:
            while heights[i] < stack[-1]:
                pop()
                w = i - popped index
                h = popped height
                max_area = max(w * h, max_area)
            stack.append(heights[i], popped index)

       
        STEP 2: pop monotonically increasing stack till empty
        
        i = len(heights)
        while stack:
            pop()
            w = i - popped index
            h = popped height
            max_area = max(w * h, max_area)

        
        DONE: return max_area

        """






