class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        monotonically decreasing queue - one way of finding max/min

        max always falls to front of queue
        when window slides, 

        if 2 not in window, then deqeue it
        enqueue [index, num]

        if num not in window anymore (using index) then dequeue it

                 L   R       
        nums= [1,2,1,0,4,2,6]

        deq = [
            2 1 0
        ]

        res = [
            2 2
        ]

        """

        deq = deque()
        res = []

        # sliding window algo - fixed k
        L = 0

        for R in range(len(nums)):
            # expand window - add to queue
            while deq and nums[R] > deq[-1][0]:
                deq.pop()
            deq.append((nums[R], R)) # (val, index)

            # shrink window - pop from queue
            while R-L+1 > k:
                if nums[L] == deq[0][0] and L == deq[0][1]:
                    deq.popleft()
                L += 1
                
            # update res only if valid window
            if (R-L+1) >= k:
                res.append(deq[0][0])
        
        return res
