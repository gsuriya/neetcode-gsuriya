class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0
        for n in nums:
            # if start of seq, start counting
            if n-1 not in nums_set:
                curr = 1
                while n+1 in nums_set:
                    curr += 1
                    n += 1
                max_length = max(curr, max_length)

        return max_length





























        # make sure I understand the problem first, cus i did this BS and i coulda just use max function to update max value dynamically instead of using bucket sort too
        # # use bucket sort to map sequence lengths
        # # index = seq length
        # seq_lengths = [[] for i in range(len(nums))]

        # # find all sequence lengths, add to list
        # count = 1
        # for i in range(1, len(nums)-1):
        #     if nums[i] - nums[i-1] == 1:
        #         count += 1
        #     else:
        #         count = 1
        #     seq_lengths[count].append(count)

        # # loop backwards, extract largest seq length
        # for i in range(len(seq_lengths)-1, 0, -1):
        #     if len(seq_lengths[i]) > 0:                                     
        #         return seq_lengths[i].pop()