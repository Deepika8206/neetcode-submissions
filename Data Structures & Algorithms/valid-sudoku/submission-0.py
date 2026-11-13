class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                r = board[i][j]
                c = board[j][i]
                if r != '.':
                    if r in row:
                        return False
                    row.add(r)
                if c != '.':
                    if c in col:
                        return False
                    col.add(c)
        for row in range(0,9,3):
            for col in range(0,9,3):
                box = set()
                for i in range(row , row+3):
                    for j in range(col , col+3):
                        num = board[i][j]
                        if num != '.':
                            if num in box:
                                return False
                            box.add(num)
        return True