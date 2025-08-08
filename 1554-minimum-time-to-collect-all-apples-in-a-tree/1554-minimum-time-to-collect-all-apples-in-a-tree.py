from collections import deque

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # First BFS, constructs parents
        parents = {}
        queue = deque([0])
        visited = set()
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parents[neighbor] = node
                    queue.append(neighbor)

        # Second BFS starting from apples, finds unique edges to root
        apples = [i for i in range(n) if hasApple[i]]
        queue = deque(apples)
        visited = set()
        res = 0

        while queue:
            node = queue.popleft()
            if node == 0 or node in visited:
                continue
            res += 2
            visited.add(node)
            queue.append(parents[node])

        return res