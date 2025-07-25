class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # represents four directions of a point
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # function to check wether a current point is inbound or out of bound
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

        def traversal(i, j):
            grid[i][j] = "0"
            for a, b in dir:
                newi, newj = a +i , j + b
                if inbound(newi, newj) and grid[newi][newj] == "1":
                    traversal(newi, newj)
        # Grid Traversal
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    traversal(i, j)
                    islandCount +=1
        
        # BFS - Breadth first search. queue 

        

        return islandCount

            