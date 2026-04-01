class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        prefix_to_i = {0: 1} # prefix_sum --> # of times it has appeared
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            # can k expand backwards?
            if curr_sum-k in prefix_to_i:
                res += prefix_to_i[curr_sum-k]

            prefix_to_i[curr_sum] = prefix_to_i.get(curr_sum, 0) + 1
        
        return res
    
