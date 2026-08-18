class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        1. freq_map
        2. bucket sort
        - indices r frequencies 
        - vals r lists (diff nums can hv same freq)
        3. extract k elements from the right

        freq_map = {
            1: 1
            2: 2
            3: 3
        }

                                      i
        bucket_sort = [[], [1], [2], [3]]

        """

        # create freq_map
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        # bucket sort - indices r freqs
        bucket_sort = [[] for i in range(len(nums)+1)] # +1 cus num could be all of nums
        for val, freq in freq_map.items():
            bucket_sort[freq].append(val)
        
        # extract top k elements from the right
        res = []
        count = k
        for i in range(len(bucket_sort)-1, -1, -1):
            while bucket_sort[i] and count:
                res.append(bucket_sort[i].pop())
                count -= 1
        return res



