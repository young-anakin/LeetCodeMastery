class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        ans = list()

        dependents = defaultdict(list)
        safeCount = defaultdict(int)

        for i, val in enumerate(graph):

            for j in val:
                dependents[j].append(i)
                safeCount[i] +=1
        
        safeNodes = deque()
        for i in range(len(graph)):
            if safeCount[i] == 0:
                safeNodes.append(i)
        
        while safeNodes:
            val = safeNodes.popleft()
            ans.append(val)
            for ind in dependents[val]:
                safeCount[ind] -=1
                if safeCount[ind] == 0:
                    safeNodes.append(ind)
        
        ans.sort()
        return ans


