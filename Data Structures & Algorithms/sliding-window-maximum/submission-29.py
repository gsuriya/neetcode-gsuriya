class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        L 
            R
        1 2 2 0 1 2 6
        
        window = [
            2 2
        ]
        res = [2, ]

        """

        res = []
        L = 0
        window = deque()

        for R in range(len(nums)):
            # expand - append to deque, larger element drops
            while window and nums[R] > window[-1]:
                window.pop()
            window.append(nums[R])

            # shrink - deqeue as shrinking
            while R-L+1 > k:
                if nums[L] == window[0]:
                    window.popleft()
                L += 1

            # update
            if R-L+1 == k:
                res.append(window[0])
        
        return res

