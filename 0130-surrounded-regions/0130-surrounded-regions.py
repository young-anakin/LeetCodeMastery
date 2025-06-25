class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])
       
        edges = set()

        visited = set()
        def dfs(i, j):
            if not inbound(i, j):
                return
            
            if board[i][j] == "X":
                return
            
            visited.add((i, j))
            for xi, xj in dir:
                newI, newJ = xi + i, xj + j
                if (newI, newJ) not in visited:
                    dfs(newI, newJ)


        
        for i in range(len(board)):
            for j in range(len(board[0])):
                for di, dj in dir:
                    if not inbound(di + i, dj + j):
                        edges.add((i, j))
                        break
        
        edges = list(edges)
        # print(edges)

        for i, j in edges:
            if board[i][j] == "O":
                dfs(i, j)
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        
        return board
        
        # print(visited)