class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        memo = defaultdict(int)
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(i, j):
            return i >=0 and j>=0 and i < len(mat) and j < len(mat[0])

        ans = [[100 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        queue = deque()
        visited = set()
        for ind in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[ind][j] == 0:
                    ans[ind][j] = 0
                    queue.append((ind, j))
                    visited.add((ind, j))
        
        while queue:
            i, j = queue.popleft()
            for up, right in dir:
                newi, newj = i + up, right + j
                if inbound(newi, newj) and (newi, newj) not in visited:
                    ans[newi][newj] = 1 + ans[i][j]
                    queue.append((newi, newj))
                    visited.add((newi, newj))
        
        return ans


        