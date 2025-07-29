class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n , visited = len(grid), len(grid[0]), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        visited = set()
        def dfs(i, j):
            if not(inbound(i,j)) or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            fin = 0
            for a, b in directions:
                ans = dfs(i + a, b + j)
                if ans != None:
                    fin += ans

            return fin

        for ind in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[ind][j] == 1:
                    return dfs(ind, j )

        return 0