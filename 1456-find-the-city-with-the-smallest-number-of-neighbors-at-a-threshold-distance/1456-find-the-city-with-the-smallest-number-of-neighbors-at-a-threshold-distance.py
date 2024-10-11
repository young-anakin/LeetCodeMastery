class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dd = defaultdict(list)
        for src, dst, w in edges:
            dd[src].append((w, dst))
            dd[dst].append((w, src))
        ans = 0
        mx = float("inf")

        for ind in range(n):
            heap = []
            # for val in dd[ind]:
            #     heapq.heappush(heap, val)
            
            heapq.heappush(heap, (0, ind))
            visited = set()
            cp = 0
            # print(heap)
            while heap:
                w, curr = heapq.heappop(heap)

                if curr in visited:
                    continue

                visited.add(curr)

                for nw, dst in dd[curr]:
                    if w + nw <= distanceThreshold:
                        # visited.add(dst)
                        heapq.heappush(heap, (nw + w , dst))
                        cp +=1
                
            #     print(heap)
            
            # print(ind, len(visited))
                
            if len(visited) <= mx:
                ans = max(ind, ans)
                mx = min(len(visited), mx)
        
        return ans

                
            