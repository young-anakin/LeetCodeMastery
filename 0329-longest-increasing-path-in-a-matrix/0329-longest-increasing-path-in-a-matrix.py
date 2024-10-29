class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        ans = [[0 for _ in range(len(grid[0]))] for ind in range(len(grid))]

        def inbound(ind, j):
            return ind >=0 and j >= 0 and ind < len(grid) and j < len(grid[0])
        
        dir = [(0,1), (1, 0), (-1, 0), (0, -1)]
        def dp(ind, j):
            if ans[ind][j] != 0:
                return ans[ind][j]
            


            for a, b in dir:
                if inbound(a+ind, j+b) and grid[a+ind][j+b] > grid[ind][j]:
                    ans[ind][j] = max(ans[ind][j], 1 + dp(a+ind, j+b))
            

            return ans[ind][j]
        
        mx = 0
        for ind in range(len(grid)):
            for j in range(len(grid[0])):
                mx = max(mx, dp(ind, j))
        
        return mx+1
