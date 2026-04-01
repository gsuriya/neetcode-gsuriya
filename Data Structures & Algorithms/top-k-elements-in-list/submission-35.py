class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        create freq_list

        bucket sort freq_list

        return k frequent elements

        """

        freq_map = defaultdict(int) # num --> freq of num

        for n in nums:
            freq_map[n] += 1
        
        bucket_sort = [[] for i in range(len(nums)+1)]
        
        for n, freq in freq_map.items():
            bucket_sort[freq].append(n)
        
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while bucket_sort[i] and k > 0:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res


















