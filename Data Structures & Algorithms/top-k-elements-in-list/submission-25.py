class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort by freq using freq_map
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        # sort freqs by bucket sort - possible b/c sum(freqs) = len(nums)
        bucket_sort = [[] for i in range(len(nums)+1)]

        for n, freq in freq_map.items():
            bucket_sort[freq].append(n)

        # extract top k freqs
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while k > 0 and bucket_sort[i]:
                res.append(bucket_sort[i].pop())
                k -= 1
        return res
