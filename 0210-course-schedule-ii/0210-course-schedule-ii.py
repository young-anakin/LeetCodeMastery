class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        dependencies = defaultdict(int)
        for val in prerequisites:
            graph[val[1]].append(val[0])
            dependencies[val[0]] +=1
            dependencies[val[1]] +=0
        visited = set()
        queue = deque()
        # queue.append()
        ans = []
        if len(prerequisites) == 0:
            ans = [ind for ind in range(numCourses)]
            return ans
        for key, val in dependencies.items():
            if val == 0:
                queue.append(key)
                ans.append(key)
                visited.add(key)
        while queue:
            val = queue.popleft()
            for sub in graph[val]:
                dependencies[sub] -=1
                if dependencies[sub] == 0:
                    queue.append(sub)
                    ans.append(sub)
                    visited.add(sub)
        print(visited)
        if len(visited) != len(dependencies):
            return []
        for ind in range(numCourses):
            if ind not in visited:
                ans.append(ind)
        return ans