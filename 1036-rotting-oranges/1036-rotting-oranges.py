class Solution:
    def orangesRotting(self, orange: List[List[int]]) -> int:
        visited = set()
        grid = [(1,0), (-1,0), (0,1), (0,-1)]
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(orange) and j < len(orange[0])
        
        queue = deque()
        for i in range(len(orange)):
            for j in range(len(orange[0])):
                if orange[i][j] == 2:
                    queue.append(((i, j), 0))
        cp = 0
        while queue:
            a, b = queue.popleft()
            for level in grid:
                i, j = a[0] + level[0], a[1] + level[1]
                if inbound(i, j) and orange[i][j] == 1:
                    orange[i][j] = 0
                    queue.append(((i, j), b+1))
                    cp = max(cp, b+1)
        
        for i in range(len(orange)):
            for j in range(len(orange[0])):
                if orange[i][j] == 1:
                    return -1
        return cp

