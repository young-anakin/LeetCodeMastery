class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {node: float('inf') for node in range(1, n+1)}
        graph = defaultdict(list)
        for val in times:
            graph[val[0]].append((val[1], val[2]))
        distances[k] = 0
        processed = set()
        heap = []
        for val in times:
            if val[0] == k:
                heapq.heappush(heap, (0, k))
        
        print(heap)
        print(graph)
        while heap:
            dist, Curr_node = heapq.heappop(heap)
            if Curr_node  in processed:
                continue
            
            processed.add(Curr_node)
            print(processed)
            for val in graph[Curr_node]:
                new_dist = dist + val[1]
                if distances[val[0]] > new_dist:
                    distances[val[0]] = new_dist
                    heapq.heappush(heap, (new_dist, val[0]))
        mx = 0
        print(distances)
        for key, value in distances.items():
            mx = max(mx, value)
        if mx == float("inf"):
            return -1
        return mx
