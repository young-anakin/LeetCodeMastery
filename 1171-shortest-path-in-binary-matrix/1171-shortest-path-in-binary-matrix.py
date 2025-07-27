class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
         n * n
         constarints is that n = 100
         Goal - we go through starting from 0, 0 to n-1, n-1

         Traversal path is 8 directional

         Approach : A pure BFS from start point to end point
        '''

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def inbound(i, j):
            return i >= 0 and j >=0 and i < len(grid) and j < len(grid[0])
        mn = float("inf")
        n = len(grid)
        def bfs(i, j):
            nonlocal mn, n

            queue = deque()

            queue.append((i, j, 0))
            visited = set()
            while queue:
                i, j, currD = queue.popleft()
                if i == n-1 and j == n-1:
                    mn = min(mn, currD)
                for dx, dy in dir:
                    newi, newj = dx + i, dy + j
                    if (newi, newj) not in visited and inbound(newi, newj) and grid[newi][newj] == 0:
                        visited.add((newi, newj))
                        queue.append((newi, newj, currD + 1))
                
 
        bfs(0, 0)
        if grid[0][0] == 1 or mn == float("inf"):
            return -1
        
        return mn + 1