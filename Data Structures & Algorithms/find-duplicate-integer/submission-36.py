class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

        duplicate # is the head of cycle

        linked list is a LL OF ARRAY INDICES

        [1, 2, 3, 2, 2]

        0 --> 1 --> 2 --> 3 
                    ^     |
                    |     |
                    -------

        """

        # fast and slow pointers until they intersect
        fast, slow = 0, 0
        while True: # they will eventually intersect since cycle is guarenteed
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        # start slow2 pointer, move slow and slow2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow2

            
        


        