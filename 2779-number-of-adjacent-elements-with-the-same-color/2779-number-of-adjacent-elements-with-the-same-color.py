class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        colors = [0 for _ in range(n)]
        cp = 0
        if n == 1:
            return [0] * len(queries)
        for ind, val in queries:
            if ind == 0:
                if colors[ind] == colors[ind+1] and colors[ind] != 0:
                    cp -=1
                colors[ind] = val
                if colors[ind] == colors[ind+1] and colors[ind] != 0:
                    cp +=1
                ans.append(cp)
            elif ind == n-1:
                if colors[ind] == colors[ind-1] and colors[ind] != 0:
                    cp -=1
                colors[ind] = val
                if colors[ind] == colors[ind-1] and colors[ind] != 0:
                    cp +=1
                ans.append(cp)
            else:
                if colors[ind] == colors[ind-1] and colors[ind] != 0:
                    cp -=1
                if colors[ind] == colors[ind+1] and colors[ind] != 0:
                    cp -=1
                
                colors[ind] = val
                if colors[ind] == colors[ind-1] and colors[ind] != 0:
                    cp +=1
                if colors[ind] == colors[ind+1] and colors[ind] != 0:
                    cp +=1
                ans.append(cp)
        return ans