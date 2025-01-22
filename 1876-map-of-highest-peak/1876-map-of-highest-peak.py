class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = set()
        queue = deque()

        ans = [[0 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]
        print(ans)
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
        
        def inbound(i, j):
            return i < len(isWater) and j < len(isWater[0]) and i >= 0 and j >= 0

        # for ind in range(len(isWater)):
        #     for j in range(len(isWater[0])):
        #         if ans[ind][j] == 0:
        #             queue.append((ind, j))
        # print(queue)
        # print(ans)
        while queue:
            a, b = queue.popleft()
            visited.add((a, b))
            mn = ans[a][b] + 1
            # for i, j in dir:
            #     newa, newb = i + a, j + b
            #     if inbound(newa, newb):   
            #         mn = min(mn, ans[newa][newb])
            
            for i , j in dir:
                newa, newb = i + a, j + b
                if inbound(newa, newb) and (newa, newb) not in visited:
                    ans[newa][newb] = mn
                    visited.add((newa, newb))
                    queue.append((newa, newb))
        
            # print(ans, (a, b))
        
        return ans


        