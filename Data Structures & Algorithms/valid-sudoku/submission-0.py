class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen_row = set()
            for j in range(len(row)):
                if row[j] in seen_row and row[j] != ".":
                    return False
                seen_row.add(row[j])
        
        for i in range(9):
            seen_col = set()
            for c in range(9):
                if board[c][i] in seen_col and board[c][i] != ".":
                    return False
                seen_col.add(board[c][i])

        for m in range(3):
            for v in range(3):
                seen_in_box = set()
                r = m*3
                z = v*3
                for l in range(r, r+3):
                    for k in range(z, z+3):
                        if board[l][k] in seen_in_box and board[l][k] != ".":
                            return False
                        seen_in_box.add(board[l][k])

        return True

                

            

                
            

        