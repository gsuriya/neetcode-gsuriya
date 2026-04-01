class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3]

        freq_map { 1:1, 2:2, 3:3 } # num --> freq

                                    i         
        bucket_sort = [ [],[1],[2],[],[],[],[] ]
        
        k = 2
        res = [3]

        """
        
        
        
        # freq_map gives most frequent elements
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # take freq_map.values(), sort them
        # use bucket_sort to sort b/c sum(freqs) = len(nums)
        # index = freq, elem = num w/ that freq
        bucket_sort = [[] for i in range(len(nums)+1)] # multiple elems can have same freq
        for num, freq in freq_map.items():
            bucket_sort[freq].append(num)

        # backwards iterate thru bucket_sort, return k largest freqs
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while bucket_sort[i] and k > 0:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res