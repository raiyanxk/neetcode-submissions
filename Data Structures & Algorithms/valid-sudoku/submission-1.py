class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(len(board)):
            for k in range(len(board[0])):

                row_num = i
                col_num = k
                num = board[i][k]

                if num == '.':
                    continue

                if num in rows[row_num]:
                    return False
                
                if num in cols[col_num]:
                    return False
                
                if num in squares[(col_num // 3, row_num // 3)]:
                    return False
                
                rows[row_num].add(num)
                cols[col_num].add(num)
                squares[(col_num // 3, row_num // 3)].add(num)

        return True
        