class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_map to get unsorted top elements
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # sort freq_map using bucket sort b/c frequencies sum up to length of string
        # index = freq, cell is nums with that freq
        bucket_sort = [[] for i in range(len(nums)+1)] 
        for num, freq in freq_map.items():
            bucket_sort[freq].append(num)

        # extract top k elements from bucket_sort array
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while len(bucket_sort[i]) > 0 and k > 0:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res