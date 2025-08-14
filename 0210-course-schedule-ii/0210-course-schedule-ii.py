class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dependents = defaultdict(list)
        dependencyAmount = defaultdict(int)
        for a, b in prerequisites:
            dependents[b].append(a)
            dependencyAmount[a] +=1
        
        print(dependents)
        independent = deque()
        ans = list()
        for i in range(numCourses):
            if dependencyAmount[i] == 0:
                independent.append(i)
                ans.append(i)
        

        completed = len(independent)
        while independent:
            val = independent.popleft()
            for ind in dependents[val]:
                dependencyAmount[ind] -=1
                if dependencyAmount[ind] == 0:
                    independent.append(ind)
                    ans.append(ind)
        
        if len(ans) != numCourses:
            return []
        return ans



