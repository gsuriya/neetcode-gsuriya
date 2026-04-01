class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        1. get frequencies of elements using freq_map
        2. bucket_sort frequencies
        3. extract top k most frequent numbers

        """

        freq_map = defaultdict(int) # num --> freq
        for n in nums:
            freq_map[n] += 1

        # lists b/c diff numbers can hv same freq
        bucket_sort = [[] for i in range(len(nums)+1)]
        for n, freq in freq_map.items():
            bucket_sort[freq].append(n)
        
        # extract
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while bucket_sort[i] and k:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res
