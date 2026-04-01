class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        k = 4

nums    4 4 4 4 4 4
pre   0 4 8 12

        there can be multiple of the same prefix sum so increment by how many you've seen so far

        """
        res = 0

        prefix_to_count = {0: 1}
        cumulative_sum = 0

        for n in nums:
            cumulative_sum += n
            
            if cumulative_sum-k in prefix_to_count: # subarray found
                res += prefix_to_count[cumulative_sum-k]
            
            # add prefix to prev map
            prefix_to_count[cumulative_sum] = prefix_to_count.get(cumulative_sum, 0) + 1
        
        return res
            

