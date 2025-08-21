class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        winners = defaultdict(int)
        ans = [ind for ind in range(len(quiet))]
        queue = deque()
        for rich in richer:
            graph[rich[0]].append(rich[1])
            winners[rich[1]] +=1
        for ind in range(len(quiet)):
            if winners[ind] == 0:
                queue.append(ind)

        while queue:
            element = queue.popleft()
            for val in graph[element]:
                # print(val, element, "element", quiet[val], quiet[element])
                if quiet[val] > quiet[element]:
                    quiet[val] = quiet[element]
                    ans[val] = ans[element]
                winners[val] -=1
                if winners[val] == 0:
                    queue.append(val)
        return ans
        
