class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """

        1 2 3 4

        1st: check 1 2 3
        2nd: check 2 3 4

        --> REPEATED WORK. just check the 3 and 4 2nd time b/c we know 3 is biggest in first check
        therefore, find max using monotonic stack/queue --> big values fall down
 

        """
        res = []

        deq = deque() # [val, i]
        L = 0

        for R in range(len(nums)):
            # expand - big fall to the bottom
            while deq and nums[R] > deq[-1][0]:
                deq.pop()
            deq.append([nums[R], R])
            
            # shrink
            while R-L+1 > k:
                # only pop left if L moved on from that elem
                if deq[0][0] == nums[L] and deq[0][1] == L:
                    deq.popleft()
                L += 1

            # update - wait until it expanded to be k size
            if R-L+1 == k:
                res.append(deq[0][0])
        
        return res