class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """

        if duplicates less than k apart
        - return True

        index_map 
        if dup ab to be added, check that is less than k apart
        if not, then set index_map[nums[i]] = i # current i is farthest apart


                i
        1 2 3 0 1 
idx       1 2 3 4

            i
        2 1 2
idx       1 2

        remove the earlier 1 from the set

        
        """
        val_to_index = {} # val --> index

        for i in range(len(nums)):
            # check if duplicate
            if nums[i] in val_to_index and i - val_to_index[nums[i]] <= k:
                return True
        
            # add to map (also overwrites previous if its there)
            val_to_index[nums[i]] = i
        
        return False
        







