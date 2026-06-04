class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """

        get rid of all triplets that have a greater value --> no point merging w/ them

        if rest of the triplets have all 3 values u want, then ur good

        """

        # make list of good triplets
        good = []
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            good.append(t)

        
        # if good triplets have values u want, then return True else False
        have = [False, False, False]
        for t in good:
            if t[0] == target[0]: have[0] = True
            if t[1] == target[1]: have[1] = True
            if t[2] == target[2]: have[2] = True
        
        for val in have:
            if not val:
                return False
        return True
        
