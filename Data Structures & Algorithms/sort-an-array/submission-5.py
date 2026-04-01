class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(L1, R1, L2, R2):
            tmp = [0] * (R2-L1+1) # copy back into L1 - R2

            # merge both arrs into tmp
            i = L1
            j = L2
            k = 0

            while i <= R1 and j <= R2:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    i += 1
                    k += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                    k += 1

            while i <= R1:
                tmp[k] = nums[i]
                i += 1
                k += 1
            while j <= R2:
                tmp[k] = nums[j]
                j += 1
                k += 1

            # copy back from tmp into actual nums array
            m = L1
            for val in tmp:
                nums[m] = val
                m += 1


        def merge_sort(L, R):
            if L >= R: # 1 element arr
                return
            
            mid = (L + R) // 2
            merge_sort(L, mid) # left
            merge_sort(mid+1, R) # right
            merge(L, mid, mid+1, R)
            
        merge_sort(0, len(nums)-1)
        return nums

    

        
            














        