class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_map: num --> freq
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # sort freqs using bucket sort O(n)
        # index = freq, val = val w/ that freq
        bucket_sort = [[] for i in range(len(nums)+1)]
        for num, freq in freq_map.items():
            bucket_sort[freq].append(num)

        # extract k elems from end of bucket_sort list
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while k > 0 and bucket_sort[i]:
                res.append(bucket_sort[i].pop())
                k -= 1

        return res

