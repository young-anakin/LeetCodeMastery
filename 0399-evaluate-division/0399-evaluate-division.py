class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for ind, val in enumerate(equations):
            graph[val[0]].append((val[1], values[ind]))
            graph[val[1]].append((val[0], 1/values[ind]))
        
        # print(graph)
        def dfs(curr, end, val, visited):
            if curr == end:
                return val
            for ind in graph[curr]:
                if ind[0] not in visited:
                    cp = visited.copy()
                    cp.add(ind[0])
                    # print(cp)
                    if dfs(ind[0], end, val * ind[1], cp):
                        return dfs(ind[0], end, val * ind[1], cp)


        ans = list()
        for a, b in queries:
            ss = set()
            ss.add(a)
            # print("cocaine", ss)
            if a not in graph or b not in graph:
                ans.append(-1)
                continue
            if not dfs(a, b, 1, ss):
                ans.append(-1)
                continue
            ans.append(dfs(a, b, 1, ss))
        
        return ans