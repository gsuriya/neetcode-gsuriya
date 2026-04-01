class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_map
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1

        # sort them
        bucket_sort = [[] for i in range(len(nums)+1)]
        for n, freq in freq_map.items():
            bucket_sort[freq].append(n)

        # extract top k most frequent
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while k > 0 and bucket_sort[i]:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res

        """

        freq_map = {
            n : freq
            1: 1
            2: 2
            3: 3
        }

        bucket_sort = [[], [1], [2], [3]]
        freq is index, number w/ that freq goes in that index
        """
