class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find if start of seq for O(n) run time
        nums_set = set(nums)

        # dynamically track longest seq
        longest = 0
        for n in nums:
            if n-1 not in nums_set: # start of seq
                # start counting longest seq
                curr = 0
                while n in nums_set:
                    n += 1
                    curr += 1
                # update longest
                longest = max(longest, curr)
        
        return longest


























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