class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        heap = []

        dd = defaultdict(int)
        edgesdd = defaultdict(list)
        visited = set()
        i = 0
        for a,b in edges:
            edgesdd[a].append((b, -1 * succProb[i]))
            edgesdd[b].append((a, -1 * succProb[i]))
            i +=1
        for ind in range(n):
            dd[ind] = float("inf")
        
        dd[start_node] = 0
        visited.add(start_node)
        for val in edgesdd[start_node]:
            heapq.heappush(heap, (val[1], val[0] ))
        
        while heap:
            mag, curr = heapq.heappop(heap)
            # print(mag, curr)
            if curr in visited:
                continue
            if curr == end_node:
                return -1 * mag
            visited.add(curr)
            # print(visited)
            for ind in edgesdd[curr]:
                if ind[0] not in visited:
                    print(ind[1])
                    heapq.heappush(heap, (-1 * mag * ind[1], ind[0]))
        # print(heap)
        return 0