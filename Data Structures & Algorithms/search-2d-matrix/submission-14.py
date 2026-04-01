class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        binary search outside
        binary search inside

                     L  m      R
        [[1,2,4,8], [10,11,12,13], [14,20,30,40]]


        """

        L, R = 0, len(matrix)-1

        while L <= R:
            mid = (L+R) // 2

            # less
            if target < matrix[mid][0]:
                R = mid-1
            # greater
            elif target > matrix[mid][-1]:
                L = mid+1
            # within
            else:
                L, R = 0, len(matrix[mid])-1

                while L <= R:
                    m = (L+R) // 2

                    if target > matrix[mid][m]:
                        L = m+1
                    elif target < matrix[mid][m]:
                        R = m-1
                    else:
                        return True
        
        return False






            