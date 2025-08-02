class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        if rows == 0:
            return 0
        
        cols = len(grid[0])
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        # to mark the outer lands as visited
        # 2 = visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(row, col):
            grid[row][col] = 2
            if inbound(row, col):
                
                for r, c in directions:
                    new_r = r + row
                    new_c = c + col
                    
                    if inbound(new_r, new_c) and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = 2
                        dfs(new_r, new_c)
                        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    flag = False
                    for r, c in directions:
                        new_r = r + i
                        new_c = c + j

                        if not inbound(new_r, new_c):
                            flag = True
                            break
                    
                    if flag:
                        dfs(i, j)
        
        number_of_islands = 0
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 0:
                    dfs(i, j)
                    number_of_islands += 1
                    
        return number_of_islands
                        
            
                
            