class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()

        remaining = defaultdict(int)
        path = defaultdict(list)
        for ind, val in enumerate(graph):
            for z in val:
                remaining[ind] +=1
                path[z].append(ind)

        queue = deque()
        for ind in range(len(graph)):
            if len(graph[ind]) == 0:
                visited.add(ind)
                queue.append(ind)

        while queue:
            val = queue.popleft()
            for ind in path[val]:
                remaining[ind] -=1
                # print(ind, val)
                if remaining[ind] == 0 and val in visited:
                    visited.add(ind)
                    queue.append(ind)
        visited =  list(visited)
        visited.sort()

        return visited