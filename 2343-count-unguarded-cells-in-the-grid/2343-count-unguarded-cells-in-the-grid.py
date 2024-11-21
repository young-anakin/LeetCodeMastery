class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = []
        for a in range(m):
            bs = []
            for b in range(n):
                bs.append(0)
            arr.append(bs)
        
        total = n*m
        for g in guards: 
            arr[g[0]][g[1]] = "G"
        
        for w in walls:
            arr[w[0]][w[1]] = "W"
        
        for i in range(len(guards)):
            total -=1
            beg = guards[i][0]
            end = guards[i][1] + 1
            while end <= n-1:
                if arr[beg][end] == "W":
                    arr[beg][end] = 'WP'
                    total -=1
                    break
                elif arr[beg][end] == "WP":
                    break
                elif arr[beg][end] == "G":
                    break
                elif arr[beg][end] == 0:
                    arr[beg][end] = 1
                    total -=1
                end +=1
            
            beg = guards[i][0]
            end = guards[i][1] - 1
            while end >= 0:
                if arr[beg][end] == "W":
                    arr[beg][end] = "WP"
                    total -=1
                    break
                elif arr[beg][end] == "WP":
                    break
                elif arr[beg][end] == "G":
                    break
                elif arr[beg][end] == 0:
                    arr[beg][end] = 1
                    total -=1
                end -=1
            
            beg = guards[i][0] - 1
            end = guards[i][1]
            while beg >= 0:
                if arr[beg][end] == "W":
                    arr[beg][end] = "WP"
                    total -=1
                    break
                elif arr[beg][end] == "WP":
                    break
                elif arr[beg][end] == "G":
                    break
                elif arr[beg][end] == 0:
                    arr[beg][end] = 1
                    total -=1
                beg -=1
            beg = guards[i][0] + 1
            end = guards[i][1]
            while beg <= m-1:
                if arr[beg][end] == "W":
                    arr[beg][end] = "WP"
                    total -=1
                    break
                elif arr[beg][end] == "WP":
                    break
                elif arr[beg][end] == "G":
                    break
                elif arr[beg][end] == 0:
                    arr[beg][end] = 1
                    total -=1
                beg +=1
            
        for a in range(m):
            for b in range(n):
                if arr[a][b] == "W":
                    total -=1
                    arr[a][b] = "WP"
        
        return total