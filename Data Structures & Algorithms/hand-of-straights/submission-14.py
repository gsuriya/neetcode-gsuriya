class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """

        put in hashmap
        - go thru freq_map in sorted order using minheap / sorted keys

        freq_map = {
            1: 1
            2: 2
            3: 2
            4: 2
            5: 1
        }

        k = 5

        1. put all unique keys in minheap
        2. peek minheap
        - start counting from there, decrementing consecutive nums in freq_map
        - if freq[n] = 0 --> remove it from heap and map
            - HOWEVER, this shld alw be the min. if we DON'T remove the min
              we create a "hole" in the remaining numbers so they're NOT consecutive
            - so return false if the n that is freq[n] = 0 is NOT the min in the minheap

        """

        # freq_map, put all keys in minheap
        freq_map = defaultdict(int)
        for c in hand:
            freq_map[c] += 1
        minh = []
        heapq.heapify(minh)
        for key in freq_map.keys():
            heapq.heappush(minh, key)
        
        # start counting from min
        while minh: # while numbers still remain
            start = minh[0]

            # count from start, decrement freq_map
            for n in range(start, start+groupSize):
                if n not in freq_map:
                    return False
                
                freq_map[n] -= 1

                # pop from heap if none of this n left
                if freq_map[n] == 0:
                    # if its not the min we're popping, hv to create hole to count consecutive --> return False
                    if n != minh[0]:
                        return False
                    
                    heapq.heappop(minh)

        return True

