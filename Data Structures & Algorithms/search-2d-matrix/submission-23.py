class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2-layered binary search

        i = -1
        L, R = 0, len(matrix)-1
        while L <= R:
            mid = (L+R) // 2

            if target > matrix[mid][-1]:
                L = mid+1
            elif target < matrix[mid][0]:
                R = mid-1
            else:
                i = mid
                break # no infinite loop now
        
        if i == -1:
            return False

        # continue search in inner array
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
