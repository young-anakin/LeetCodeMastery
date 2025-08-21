class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]

        graph = defaultdict(list)
        dep = defaultdict(int)

        for a, b in edges:
            graph[a].append(b)
            dep[b] +=1
        

        queue = deque()
        for i in range(n):
            if dep[i] == 0:
                queue.append(i)
        
        while queue:
            element = queue.popleft()
            for val in graph[element]:
                dep[val] -=1
                ans[val].add(element)
                ans[val].update(ans[element])
                if dep[val] == 0:
                    queue.append(val)
        fin = []
        for i in ans:
            i = list(i)
            i.sort()
            fin.append(i)
            # print(i)
        
        return fin
