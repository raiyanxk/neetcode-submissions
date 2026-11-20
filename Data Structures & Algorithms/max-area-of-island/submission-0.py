class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]

        def inRange(i, j, grid):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        def dfs(i, j, grid):

            if (i, j) in seen or grid[i][j] == 0:
                return 0
            
            res = 1

            seen.add((i, j))

            for dy, dx in dirs:
                if inRange(i + dy, j + dx, grid) and (i + dy, j + dx) not in seen:
                    res += dfs(i + dy, j + dx, grid)

            return res

        
        res = 0

        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 1:
                    res = max(res, dfs(i, k, grid))

        return res