class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float("inf") for ind in range(n)]
        ans = {}
        # for ind in range(n):
        #     ans[ind] = float("inf")
        # dd = defaultdict(list)
        # ans[0] = 0
        # for s, d, p in flights:
        #     dd[s].append((d,p))
        # visited =set()
        prev[src] = 0
        for ind in range(k+1):
            any_relaxation = False
            curr = prev[::]
            for u, v, w in flights:
                print(u, v, w, prev[u], curr[v])
                if prev[u] != float("inf") and prev[u] + w < curr[v]:
                    curr[v] = prev[u] + w
                    any_relaxation = True
                
            if not any_relaxation:
                break

                # print(curr)
            prev = curr[::]   
            # print("p", prev)        
        
        if prev[dst] != float("inf"):
            return prev[dst]
        
        return -1

        
