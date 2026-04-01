class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return top k frequent elements

        # freq map to find most frequent elements
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        # bucket sort the frequencies into a new array
        # indices = freq, 
        bucket_sort = [[] for i in range(len(nums)+1)] # lists b/c diff chars can have same freq
        for num, freq in freq_map.items():
            bucket_sort[freq].append(num)

        # pop k elements from bucket sort array
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while len(bucket_sort[i]) > 0 and k > 0:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res