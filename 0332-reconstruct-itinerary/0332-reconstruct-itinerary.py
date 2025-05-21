class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        path = []
        graph = defaultdict(list)
        for src, destination in tickets:
            graph[src].append(destination)
            
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            path.append(node)

        dfs("JFK")
        return path[::-1]
        