class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        cp = 0
        queue = deque()
        for key in graph.keys():
            queue.append(key)
        
        visited = set()
        while queue:
            val = queue.popleft()
            for ind in graph[val] :
                if ind not in visited:
                    visited.add(ind)
        
        if abs(len(visited) - n) != 1:
            return -1
        
        else:
            for ind in range(100):
                if ind not in visited:
                    return ind
        print(visited)