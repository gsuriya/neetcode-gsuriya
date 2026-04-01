class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        sorting does two things:
        1. allows you to skip dups when MOVING POINTERS
        2. two sum II algo to find triplet


         -1 0 1 2 -1 -4 
     
         -4 -1 -1 0 1 2


        L < R b/c i, j, j need to be unique

        only need to skip for L and R when TRIPLET FOUND b/c anyways if no triplet
        ur going to anyways increment L

        """

        res = []

        nums.sort()
        for i in range(len(nums)):
            # skip triplets with this i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i+1, len(nums)-1
            while L < R:
                sum_ = nums[i] + nums[L] + nums[R]

                if sum_ < 0:
                    L += 1
                elif sum_ > 0:
                    R -= 1
                else:
                    # triplet found
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1 # increment either L or R to find more triplets, either L or R incrementing/decrementing works the algo self corrects itself anyways
                    # skip duplicates for L cus it'll add the same triplet again
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        
        return res












        
