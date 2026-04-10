class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # we are going to check if there are duplicates in
        # the rows by adding them to a hashset
        for i in range(9):
            # we create a hashset for each row
            s = set()
            # we iterte through the columns and check if theyre
            # in the set if no add them otherwise if yes
            # the sudoku is invalid so we return false
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)


        # we are going to check if ther are duplicates in the
        # colums by adding them 
        for i in range(9):
            s = set()
            for j in range(9):
                # loop column first and row second
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        

        # for the 3 grid we are goingn to initialize the start
        # of the 9 3x3 grid and store it

        start = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        for i,j in start:
            # as we are checking all the values we initialize the 
            # hashset before both the row and column
            s = set()
            for row in range(i, i+3):
                for cols in range(j, j+3):
                    item = board[row][cols]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        
        return True
        
    
        
        
        
        