class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequency map (num --> frequency)
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # map frequencies as array indices
        freq_array = [[] for i in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            freq_array[freq].append(num)

        # .pop() k times
        return_list = []
        for i in range(len(freq_array)-1, 0, -1):
            while k > 0 and len(freq_array[i]) > 0:
                return_list.append(freq_array[i].pop())
                k -= 1
            if k == 0:
                return return_list
                