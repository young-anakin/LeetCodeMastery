class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        mx = 0
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(ind, j):
            return ind >=0 and j >= 0 and ind < len(grid) and j < len(grid[0])
        visited = set()
        def bfs(ind, j):
            sm = grid[ind][j]
            queue = deque()
            queue.append((ind, j))
            while queue:
                ind, j = queue.popleft()
                for a, b in dir:
                    newa, newb = ind + a, j + b
                    if inbound(newa, newb) and grid[newa][newb] > 0 and (newa, newb) not in visited:
                        visited.add((newa, newb))
                        sm += grid[newa][newb]
                        queue.append((newa, newb))
            
            return sm

        
        for ind in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[ind][j] > 0 and (ind, j) not in visited:
                    visited.add((ind, j))
                    mx = max(mx, bfs(ind, j))

        return mx