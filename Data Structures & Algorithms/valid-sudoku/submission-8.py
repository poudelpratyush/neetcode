class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for i in range(9):
            s = set()
            for j in range(9):
                if (board[i][j] == "."):
                    continue
                elif (board[i][j] in s):
                    return False
                s.add(board[i][j])
        
        # cols
        for i in range(9):
            s = set()
            for j in range(9):
                if (board[j][i] == "."):
                    continue
                elif (board[j][i] in s):
                    return False
                s.add(board[j][i])


        # 3x3 boxes
        start = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]

        for i, j in start:
            s = set()
            for row in range(i, i + 3):
                for cols in range(j, j + 3):
                    if (board[row][cols] == "."):
                        continue
                    elif (board[row][cols] in s):
                        return False
                    s.add(board[row][cols])

        return True





