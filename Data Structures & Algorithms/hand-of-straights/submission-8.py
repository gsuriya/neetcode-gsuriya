class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """

        SORTED KEYS SOLUTION

        freq_map = {
            1: 0
            2: 0 DELETED
          i 3: 1
            4: 1
            5: 1
        }  

        """

        # create freq_map to go through 
        freq_map = defaultdict(int)
        for n in hand:
            freq_map[n] += 1

        # go through freq_map in sorted order
        # keep using all of the number until ur done with it
        for n in sorted(freq_map.keys()):
            # keep creating groups from this n until its 0 and deleted from map
            while n in freq_map:
                for i in range(n, n + groupSize): # 1-4
                    # next consecutive num not there
                    if i not in freq_map:
                        return False

                    freq_map[i] -= 1
                    if freq_map[i] == 0: 
                        # if ur the thing ur deleting isn't the min, it ruins consecutiveness for remaining numbers
                        if i != min(freq_map):
                            return False
                        del freq_map[i]
        
        return True



            