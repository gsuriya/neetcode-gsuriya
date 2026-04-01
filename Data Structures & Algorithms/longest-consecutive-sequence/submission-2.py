class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums:
            # check if num is start of sequence to avoid O(n^2)
            if num-1 not in nums_set: # num is seq start
                # count how long the seq goes to
                curr = 0
                while num in nums_set:
                    curr += 1
                    num += 1
                longest = max(curr, longest) #dynamically keep track of max seq lenght
        
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