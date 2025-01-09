class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        mx = -1
        ss = set()

        graph = defaultdict(list)
        for ind in range(len(edges)):
            if edges[ind] == -1:
                continue
            graph[ind].append((edges[ind], 0))
            ss.add(edges[ind])

        queue = deque()
        
        # print(graph)
        # print(queue)
        visited = set()
        for ind in range(len(edges)):
            dd = defaultdict(int)

            if ind in visited or not graph[ind]:
                # print("Not", ind)
                continue
            queue.append((ind, 0))
            dd[ind] = 0
            v = set()
            fl = False
            while queue:
                a, b = queue.popleft()
                if a in visited:
                    break
                v.add(a)
                for x, j in graph[a]:
                    if x not in v:
                        dd[x] = dd[a] + 1
                        queue.append((x, j+b+1))
                    else:
                        # print(x, 'valll', b , dd[x])
                        # print('dd', dd)
                        mx = max(mx, abs(b - dd[x]) +1 )
                        fl = True
                        break
                if fl:
                    break
            # if fl:
            print(v)
            visited.update(v)

        # print(visited)
        return mx