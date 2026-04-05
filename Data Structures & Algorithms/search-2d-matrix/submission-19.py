class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        1. binary search on rows
        2. binary search on columns

        T = 10

            L           m           R
        [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

        """
        # rows
        L, R = 0, len(matrix)-1
        i = 0

        while L <= R:
            mid = (L+R) // 2

            if target > matrix[mid][-1]:
                L = mid+1
            elif target < matrix[mid][0]:
                R = mid-1
            else:
                i = mid
                break
        
        # columns
        L, R = 0, len(matrix[i])-1

        while L <= R:
            mid = (L+R) // 2

            if target > matrix[i][mid]:
                L = mid+1
            elif target < matrix[i][mid]:
                R = mid-1
            else:
                return True
        
        return False

