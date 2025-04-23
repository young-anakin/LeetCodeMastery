class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        indegree = defaultdict(list)
        dependency = defaultdict(int)

        for i, j in prerequisites:
            indegree[j].append(i)
            dependency[i] +=1
        
        processed = 0

        queue = deque()

        for i in range(numCourses):
            if dependency[i] == 0:
                queue.append(i)
                processed +=1
        print(indegree)
        print(queue)
        while queue:
            val = queue.popleft()
            processed +=1
            for i in indegree[val]:
                dependency[i] -=1
                if dependency[i] == 0:
                    queue.append(i)

        print(dependency)
        for key, val in dependency.items():
            if val > 0:
                return False
        
        return True