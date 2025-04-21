class Solution:
    def reorganizeString(self, s: str) -> str:

        # heap = heapq.heappify(s)

        ans = []
        cp = Counter(s)
        for key, val in cp.items():
            ans.append((-val, key))
        
        heapq.heapify(ans)
        fl = True
        fin = ""
        while ans:
            n, chr = heapq.heappop(ans)
            n = n * -1
            for _ in range(n-1):
                fin += chr
                if ans:
                    ko = heapq.heappop(ans)
                    fin += ko[1]
                    cp = ko[0] + 1
                    if cp < 0:
                        heapq.heappush(ans, (cp, ko[1]))
                else:
                    return ""
            fin += chr
        
        return fin


        print(ans)