class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """

        neetcode's solution
        - instead of checking that "have" boolean arr is good, u can js have a set of indices which
          are marked as "good"

        """

        good_positions = set() # set of indices in target which are found from rest of good triplets

        for t in triplets:
            # triplet is bad
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # if not, check if any positional match in this triplet w/ target
            for i, val in enumerate(t):
                if val == target[i]:
                    good_positions.add(i)

        return len(good_positions) == 3