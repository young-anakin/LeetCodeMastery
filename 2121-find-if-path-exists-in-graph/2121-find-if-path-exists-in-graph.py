class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # O(V + E)
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        


        stack = [source]
        visited = set([source])
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            for neigh in graph[node]:
                if neigh not in visited:
                    stack.append(neigh)
                    visited.add(neigh)
        
        return False
            




