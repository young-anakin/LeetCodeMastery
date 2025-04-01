class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # directions to go
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # inbound checker

        def inbound(ind, j):
            return ind >= 0 and j >=0 and ind < len(grid) and j < len(grid[0])
        
        visited = set()
        islands = 0
        def islandSizeCalculator(ind , j):
            queue = deque()
            queue.append((ind, j))
            visited.add((ind, j))
            while queue:
                ind, j = queue.popleft()
                for horiz, vert in dirs:
                    new_i, new_j = ind + horiz, j + vert
                    if inbound(new_i, new_j) and (new_i, new_j) not in visited and grid[new_i][new_j] == "1":
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j ) not in visited:
                    island +=1
                    islandSizeCalculator(i, j)

        return island
                    