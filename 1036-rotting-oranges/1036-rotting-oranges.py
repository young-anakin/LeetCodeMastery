class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        dir = [(1, 0), (0, -1), (-1, 0), (0,1)]

        def inbound(i, j):
            return i >= 0 and j>=0 and i < len(grid) and j < len(grid[0])

        
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i, j), 0))
                    grid[i][j] = 0

        mx = 0
        while queue:
            coord,  time = queue.popleft()
            for xi, xj in dir:
                newi, newj = coord[0] + xi, coord[1] + xj
                if inbound(newi, newj) and grid[newi][newj] == 1:
                    queue.append(((newi, newj), time+1))
                    grid[newi][newj] = 0
                    mx = max(time+1, mx)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mx


