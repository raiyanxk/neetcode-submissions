class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # multi source bfs

        inf = 2**31 - 1

        def valid(cell):
            y, x = cell
            return  y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]) and grid[y][x] == inf
        
        q = collections.deque()

        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 0:
                    q.append((i, k))
        
        steps = 1

        while q:

            curr_len = len(q)

            for _ in range(curr_len):
                curr_y, curr_x = q.popleft()

                directions = [-1, 0, 1]

                for dy in directions:
                    for dx in directions:
                        if abs(dy) != abs(dx) and valid((curr_y + dy, curr_x + dx)):
                            grid[curr_y + dy][curr_x + dx] = steps
                            q.append((curr_y + dy, curr_x + dx))
            
            steps += 1

        