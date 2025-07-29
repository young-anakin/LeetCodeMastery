class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        fl = False
        def dfs(node, visited):
            nonlocal fl
            # 2 == destination
            if node == destination:
                fl = True 
                return True
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    if dfs(neigh, visited):
                        return True
        
        dfs(source, set())
        return fl

