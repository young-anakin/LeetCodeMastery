class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dd = defaultdict(int)
        tot = 0
        ans = []
        balls = defaultdict(int)
        colors = defaultdict(int)
        for a, b in queries:
            if balls[a] == 0:
                balls[a] = b
                if colors[b] == 0:
                    tot +=1
                else:
                    pass
                colors[b] +=1
            else:
                x = balls[a]
                colors[x] -=1
                if colors[x] == 0:
                    balls[a] = b
                    tot -=1
                    if colors[b] == 0:
                        tot +=1
                    else:
                        pass
                else:
                    balls[a] = b
                    if colors[b] == 0:
                        tot +=1
                    else:
                        pass

                colors[b] +=1
            ans.append(tot)
        
        return ans

