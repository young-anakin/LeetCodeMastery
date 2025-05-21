from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # number of connected components == n
        # number of edges has to be n -1 -> no cycle

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        edges = 0
        components = 0
        queue = deque()
        queue.append(0)
        visited.add(0)

        while queue:
            ind = queue.popleft()
            edges += len(graph[ind])
            components +=1
            for key in graph[ind]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        
        if components == n and edges/2 == n -1:
            return True
        return False
        print(edges, components)


                    

