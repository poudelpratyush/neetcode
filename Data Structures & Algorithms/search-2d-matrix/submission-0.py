class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix) - 1
        has = False
        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                has = True
                break
        
        if has == False:
            return False
    
        row = (top + bot) // 2
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid1 = (l + r) // 2
            if target > matrix[row][mid1]:
                l = mid1 + 1
            elif target < matrix[row][mid1]:
                r = mid1 - 1
            else:
                return True
        return False
