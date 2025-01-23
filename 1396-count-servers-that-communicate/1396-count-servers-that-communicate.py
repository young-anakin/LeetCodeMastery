class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        queue = deque()
        row = len(grid[0])
        col = len(grid)

        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(ind, j):
            return ind >= 0 and j >= 0 and ind < len(grid) and j < len(grid[0])
        visited = set()
        cp = 0
        def bfs(queue):
            cp = 0
            while queue:
                a, b = queue.popleft()
                # visited.add((a, b))
                for i in range(row+1):
                    newa, newb = a, 0 + i
                    if inbound(newa, newb) and grid[newa][newb] == 1 and (newa, newb) not in visited:
                        cp +=1
                        visited.add((newa, newb))
                        queue.append((newa, newb))
                        # print(newa, newb)
                
                for i in range(col+1):
                    newa, newb = 0+i, b
                    if inbound(newa, newb) and grid[newa][newb] == 1 and (newa, newb) not in visited:
                        cp +=1
                        visited.add((newa, newb))
                        queue.append((newa, newb))
                        # print(newa, newb)


            
            return cp

            # print(queue)
        ans = 0
        for ind in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[ind][j] == 1 and (ind, j) not in visited:
                    queue = deque()
                    visited.add((ind, j))
                    queue.append((ind, j))
                    x = (bfs(queue))
                    # print(x, (ind, j))
                    if x != 0:
                        ans += x+1
        return ans