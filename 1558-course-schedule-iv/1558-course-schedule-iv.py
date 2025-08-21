class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        dep = defaultdict(int)

        ancestors = defaultdict(set)
        for i in range(numCourses):
            ancestors[i].add(i)

        for a, b in prerequisites:
            graph[a].append(b)
            dep[b] +=1
        
        queue = deque()
        # for i in range(numCourses):
        #     if dep[i] == 0:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        for i in range(numCourses):
            if dep[i] == 0:
                queue.append(i)
        
        while queue:
            element = queue.popleft()
            for val in graph[element]:
                dep[val] -=1
                if dep[val] == 0:
                    queue.append(val)
                ancestors[val].add(element)
                ancestors[val].update(ancestors[element])

        ans = []
        for a, b in queries:
            if a in ancestors[b]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans