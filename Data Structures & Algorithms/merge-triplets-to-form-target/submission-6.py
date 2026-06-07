class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """

        1. can't merge any triplet w/ higher position --> get rid of these
        2. if all 3 numbers exist in their postions that match target
        - possible to get it --> return True
        - return False if not all 3 indices found

        """

        good = set()

        for t in triplets:
            # skip if one of the positions is greater than target, no point in merging w/ this triplet
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]: good.add(0)
            if t[1] == target[1]: good.add(1)
            if t[2] == target[2]: good.add(2)
        
        return len(good) == 3 # all 3 positions in target can be reached