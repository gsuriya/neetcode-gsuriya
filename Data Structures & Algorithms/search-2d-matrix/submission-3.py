class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. choose row using binary search
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            # if target greater than last index
            if target > matrix[mid][-1]:
                l = mid+1
            # if target less than first index
            elif target < matrix[mid][0]:
                r = mid-1
            # else target between inclusive 1st and last index
            else:
                # 2. perform binary search within row
                l, r = 0, len(matrix[mid])-1

                while l <= r:
                    mid2 = (l+r)//2

                    if target > matrix[mid][mid2]:
                        l = mid2+1
                    elif target < matrix[mid][mid2]:
                        r = mid2-1
                    else:
                        return True
        
        return False