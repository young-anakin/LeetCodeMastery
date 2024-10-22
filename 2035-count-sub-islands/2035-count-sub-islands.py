class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dir = [(1,0), (0,1), (-1, 0), (0,-1)]
        def inbound(i, j):
            return i >= 0  and j >= 0 and i < len(grid1) and j < len(grid2[0])
        # def bfs(i, j):
        #     visited = set()
        #     queue = deque()
        #     if grid1[i][j] == 1:
        #         queue.append((i, j))
        #     while queue:
        #         val = queue.popleft()
        #         for a, b in dir:
        #             new_a, new_b = a + val[0], b + val[1]
        #             if inbound(new_a, new_b) and grid1[new_a][new_b] == 1 and (new_a, new_b) not in visited:
        #                 queue.append((new_a, new_b))
        #                 visited.add((new_a, new_b))
        #     return visited
        def bfs2(i, j):
            queue = deque()
            if grid2[i][j]:
                queue.append((i, j))
            grid2[i][j] = 0
            fl = True
            while queue:
                val = queue.popleft()
                for a, b in dir:
                    new_a, new_b = a + val[0], b + val[1]
                    if inbound(new_a, new_b) and grid2[new_a][new_b] == 1 and grid1[new_a][new_b] == 0:
                        fl = False
                    if inbound(new_a, new_b) and grid2[new_a][new_b] == 1 and grid1[new_a][new_b] == 1:
                        grid2[new_a][new_b] = 0
                        queue.append((new_a, new_b))
            if fl:
                return 1
            else:
                return 0
        seen = set()
        cp = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 1:

                    cp += bfs2(i, j)
        # print(grid2)
        return cp