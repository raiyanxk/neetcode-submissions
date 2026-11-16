class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        height = len(board)
        width = len(board[0])

        for i in range(height):
            for j in range(width):
                c = board[i][j]
                square = (i // 3, j // 3)

                if c == '.':
                    continue 

                if c in rows[i] or c in cols[j] or c in squares[square]:
                    return False
                
                rows[i].add(c)
                cols[j].add(c)
                squares[square].add(c)
        

        return True 
                        