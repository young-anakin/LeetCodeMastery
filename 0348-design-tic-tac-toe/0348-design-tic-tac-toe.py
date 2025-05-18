from collections import deque

class TicTacToe:
    def __init__(self, n: int):
        self.grid = [['_' for _ in range(n)] for _ in range(n)]
        self.n = n
        
    def inbound(self, i, j):
        return 0 <= i < self.n and 0 <= j < self.n
    
    def check(self, up, down, player):
        directions = [
            (0, 1),  # horizontal
            (1, 0),  # vertical
            (1, 1),# diagonal
            (1, -1) # anti-diagonal
        ]
        
        for dx, dy in directions:
            queue = deque()
            queue.append((up, down))
            visited = set()
            visited.add((up, down))
            count = 1
            
            while queue:
                i, j = queue.popleft()
                for x, y in [(dx, dy), (-dx, -dy)]:
                    new_x, new_y = i + x, j + y
                    if self.inbound(new_x, new_y) and (new_x, new_y) not in visited:
                        if self.grid[new_x][new_y] == player:
                            queue.append((new_x, new_y))
                            visited.add((new_x, new_y))
                            count += 1
                        else:
                            break
            if count >= self.n:
                return True
            
        return False

    def move(self, row: int, col: int, player: str) -> bool:
        self.grid[row][col] = player
        if self.check(row, col, player):
            return player
        return 0
        return self.check(row, col, player)

# # Example usage:
# n = 3
# game = TicTacToe(n)
# print(game.move(0, 0, 'X'))  # Place X at (0, 0)
# print(game.move(0, 1, 'X'))  # Place X at (0, 1)
# print(game.move(0, 2, 'X'))  # Place X at (0, 2)
