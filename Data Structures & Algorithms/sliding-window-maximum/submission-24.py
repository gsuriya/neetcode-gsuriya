class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        ways to find max:
        1. monotonic stack (THIS ONE)
        2. heaps
        2. dynamically updating max

                     L
                           R
        [1  2  1] 0  4  2  6       2
        1 [2  1  0] 4  2  6        2
        1  2 [1  0  4] 2  6        4
        1  2  1 [0  4  2] 6        4
        1  2  1  0 [4  2  6]       6

        decreasing_deque = [
            6
        ]

        if elem being removed from window is front of q, q.popleft()


        """
        res = []

        L = 0
        q = deque()

        for R in range(len(nums)):
            # expand - keep decreasing monotonic stack
            while q and nums[R] > q[-1]:
                q.pop()
            q.append(nums[R])

            # shrink - if window size > k
            while R-L+1 > k:
                # if L ab to remove front of q, then dequeue
                if nums[L] == q[0]:
                    q.popleft()
                L += 1

            # append max elem (front of q)
            if R-L+1 == k:
                res.append(q[0])


        return res
        





