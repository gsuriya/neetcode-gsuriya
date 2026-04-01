class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        sorting does two things
        1. allows for skipping duplicates when moving pointers (MAIN THING)
        2. two sum II logic to find sum_ = 0

        this problem is quite simple
        only two rules are this
        1. sort
        2. when moving pointers, move it to a nonduplicate


        -1 0 1 2 -1 -4 

         i  L       R
        -1 -1 0 1 2 4

        """

        res = []
        nums.sort() # allows for moving past duplicates

        for i in range(len(nums)):
            # move i past duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # two sum II algo
            L, R = i+1, len(nums)-1
            while L < R: # no duplicate triplets so < not <=
                sum_ = nums[i] + nums[L] + nums[R] 

                if sum_ < 0:
                    L += 1
                elif sum_ > 0:
                    R -= 1
                else:
                    # need to care ab dups when moving pointers b/c don't want to add duplicates
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    # move L if it landed on a duplicate
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

        return res







