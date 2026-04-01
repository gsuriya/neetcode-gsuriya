class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        binary search on outer lists
        binary search on inner numbers

        """

        L, R = 0, len(matrix)-1

        while L <= R:
            mid = (L+R) // 2

            # check mid
            if target > matrix[mid][-1]:
                L = mid+1
            elif target < matrix[mid][0]:
                R = mid-1
            else:
                # inner binary search
                arr = matrix[mid]
                L, R = 0, len(arr)-1

                while L <= R:
                    mid = (L+R) // 2

                    if arr[mid] > target:
                        R = mid-1
                    elif arr[mid] < target:
                        L = mid+1
                    else:
                        return True
        
        return False





            