class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for u, v, w in edges:
            self.graph[u].append((v, w))
        
        print(self.graph)

    def addEdge(self, edge: List[int]) -> None:

        self.n +=1
        self.graph[edge[0]].append((edge[1], edge[2]))

        print(self.graph)
        

    def shortestPath(self, node1: int, node2: int) -> int:
        dd = defaultdict(int)
        for ind in range(self.n):
            dd[ind] = float("inf")
        
        dd[node1] = 0

        queue = list()
        queue.append((node1, 0))

        while queue:
            node, currdist = heapq.heappop(queue)

            if currdist > dd[node]:
                continue        

            for neighbour, w in self.graph[node]:
                new = w + currdist

                if dd[neighbour] >= new:    
                    dd[neighbour] = new
                    heapq.heappush(queue, (neighbour, new))

        if dd[node2] == float("inf"):
            return -1

        return dd[node2]  


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)