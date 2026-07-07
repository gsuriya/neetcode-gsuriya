class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        1. freq_map to find most frequent elements
        2. bucket sort them into buckets
        - possible b/c maxfreq bounded by length of nums
        3. extract top k from reverse

        """

        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1

        bucket_sort = [[] for _ in range(len(nums)+1)]
        for n, f in freq_map.items():
            bucket_sort[f].append(n)
        
        count = k
        res = []
        for i in range(len(bucket_sort)-1, -1 ,-1):
            while bucket_sort[i] and count:
                res.append(bucket_sort[i].pop())
                count -= 1
        
        return res






