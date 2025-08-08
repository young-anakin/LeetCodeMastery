class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        target = len(graph)-1
        result = list()
        queue.append((0, [0]))

        dd = defaultdict(list)
        for i, val in enumerate(graph):
            dd[i].extend(val)

        # print(dd)
        # path = [ptr, ptr, ptr, ptr]
        # path = [0, 1, 2]
        # new_path = [0,1]
        # new_path = [0,2]
        while queue:
            # currval, array
            curr, path = queue.popleft()
            # print(curr, path)
            if curr == target:
                result.append(path)
                continue
            
            for neigh in dd[curr]:
                # print("Neight", neigh)
                new_path = path.copy()
                new_path.append(neigh)
                queue.append((neigh, new_path)) 
        
        return result
            

            

            
