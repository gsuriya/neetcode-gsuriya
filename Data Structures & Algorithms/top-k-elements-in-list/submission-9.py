class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the top k modes
        # big jon prepping for PEG interview rn friday 4:30

        # use frep_map to get modes
        freq_map = defaultdict(int) # num --> freq
        for num in nums:
            freq_map[num] += 1
    

        # since freq constrained by n, bucket sort
        bucket_sort = [[] for i in range(len(nums)+1)]
        for num, freq in freq_map.items():
            bucket_sort[freq].append(num)

        # extract k modes from bucketsort output list
        res = []
        for i in range(len(bucket_sort)-1, -1, -1):
            while k > 0 and len(bucket_sort[i]) > 0:
                res.append(bucket_sort[i].pop())
                k -= 1
        
        return res
