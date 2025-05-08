class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a, b inorder to take course a, you have to take course b

        dependency = defaultdict(int)
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            dependency[a] +=1
        
        queue = deque()
        ans = []
        visited = set()
        for i in range(numCourses):
            if dependency[i] == 0:
                queue.append(i)
                visited.add(i)
                ans.append(i)
        # visited = set()
        while queue:
            val = queue.popleft()
            for i in graph[val]:
                dependency[i] -=1
                if dependency[i] == 0:
                    visited.add(i)
                    queue.append(i)
                    ans.append(i)
        
        if len(visited) == numCourses:
            return ans
        return []
