class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """

        build a hashmap -> longest consecutive sequence problem basically

        go through hashmap keys in sorted order:
        1. minheap
        2. sorted(keys)
        each of these are equivalent ways to go in sorted order

        NOTE: if middle val becomes 0 in sequence, return false
              cus consecutiveness of rest of numbers ruined

        MINHEAP SOLUTION

       

        """
        # edge case: can't even be split into equal groups
        if len(hand) % groupSize != 0:
            return False
        
        # create freq_map 
        freq_map = defaultdict(int)
        for n in hand:
            freq_map[n] += 1

        # push all keys to minheap to sort
        minh = []
        heapq.heapify(minh)
        for key in freq_map:
            heapq.heappush(minh, key)
        
        """

         freq_map = {
            1: 0
            2: 1
            3: 1
            4: 1
            5: 1
        }

        minh = [2, 3, 4, 5]

        """
        # go through sorted keys in freq_map using minheap
        while minh: # only remove key when freq = 0
            # count groups from the start and decrement
            start = minh[0]
            for n in range(start, start + groupSize):# 1-4
                # next consecutive num not there
                if n not in freq_map: 
                    return False
                freq_map[n] -= 1

                # after decrementing if freq = 0 pop from heap so we don't process it again
                if freq_map[n] == 0:
                    if n != minh[0]: # not popping the min, putting a hole in consecutive order
                        return False
                    heapq.heappop(minh) # done using all of this number
                    # del freq_map[n] # don't rlly hv to but its just easier to think ab
        
        return True

        



