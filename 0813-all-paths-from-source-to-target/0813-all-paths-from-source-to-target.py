class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        end = len(graph)-1

        traverse = defaultdict(list)

        for i, val in enumerate(graph):
            traverse[i].extend(val)
        

        visited = set()
        queue = deque()
        queue.append((0, [0]))
        ans = []
        while queue:
            val, arr = queue.popleft()
            if val == end:
                ans.append(arr)
            # visited.add(val)
            for i in traverse[val]:
                # if i in visite
                tmp = arr[:]
                tmp.append(i)
                queue.append((i, tmp))
                # visited.add(i)
        
        return ans



        # print(traverse)