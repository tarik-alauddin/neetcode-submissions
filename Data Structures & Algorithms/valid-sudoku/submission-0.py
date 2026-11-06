class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # len and width of board are equal
        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]

                if val == ".":
                    continue

                if (val in rows[r] or 
                val in cols[c] or 
                val in squares[(r//3, c//3)]):
                    print("row: ", r, " col: ", c, " val: ", val)
                    print(r, c//3, squares[(r//3, c//3)])
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)

        return True
