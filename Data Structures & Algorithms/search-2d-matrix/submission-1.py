class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix - rows ascending order
        # first int row > prev row last int
        # O(log m*n) --> basically j binary search algo on 2D arra

        """
        target = 10

        l = 0
        r = 2
        mid = (0 + 2) // 2 --> say its 0 for

              0             1              2 
        [  [1,2,4,8]  [10,11,12,13]  [14,20,30,40] ]

        if target > 13
            go to right array 

        elif target < 10
            go to left array

        else: 10 <= target <= 13
            go into this array, binary search 10

        """

        # first binary search outside 
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l + r) // 2
            
            if target > matrix[mid][-1]:
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else: # binary search for target
                l = 0
                r = len(matrix[mid])-1

                while l <= r:
                    mid2 = (l+r) // 2

                    if target > matrix[mid][mid2]:
                        l = mid2+1
                    elif target < matrix[mid][mid2]:
                        r = mid2-1
                    else:
                        return True
        
        return False

