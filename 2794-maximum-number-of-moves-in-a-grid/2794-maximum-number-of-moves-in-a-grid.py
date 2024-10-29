class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # print(grid)
        ans = [[0 for ind in range(len(grid[0]))] for j in range(len(grid))]
        dir = [(-1, 1), (0, 1), (1, 1)]
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        memo = defaultdict(int)
        visited = set()
        def dp(ind, j):
            if ans[ind][j] != 0:
                return ans[ind][j]
            
            if not inbound(ind, j):
                return 0

            for a, b in dir:
                if inbound(ind+a, j+b) and grid[ind][j] < grid[ind+a][j+b]:
                    ans[ind][j] = max(ans[ind][j], dp(ind+a, j+b)+1)
            
            return ans[ind][j]

        mx = 0
        for ind in range(len(grid)):
            # for j in range(len(grid[0])):
            mx = max(mx, dp(ind, 0))
        dp(0,0)
        # print(grid[0][1])
        # print(ans)

        return mx