class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        q: after triplet found, y can u move EITHER L or R??
           dont u miss out on combos?

        use general triplet pattern
        skip duplicates when moving pointers

         i  L                  R
        [2, 2, 2, 4, 4 , 6, 7, 8]

        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            # if duplicate first val of triplet i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # sorted, so can use Two Sum II algo            
            L, R = i+1, len(nums)-1

            while L < R:
                sum_ = nums[i] + nums[L] + nums[R]

                if sum_ > 0:
                    R -= 1 # dont needa acc for dups cus not even adding to res, it'll just move to the next
                elif sum_ < 0:
                    L += 1 # dont needa acc for dups cus not even adding to res, it'll just move to the next
                else:
                    # triplet found
                    res.append([nums[i], nums[L], nums[R]])
                    
                    # move either L or R, skip dups
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

        return res




                    

