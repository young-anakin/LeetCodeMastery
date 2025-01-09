class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        dir = [(0,1), (1,0), (-1, 0), (0, -1)]
        dist = defaultdict(int)


        def real(ind, j):
            return ind >= 0 and j >= 0 and ind < len(grid) and j < len(grid[0])
        for ind in range(len(grid)):
            for j in range(len(grid[0])):
                for d in dir:
                    if real(ind + d[0], j + d[1]):
                        if grid[ind+d[0]][j+d[1]]:
                            graph[(ind, j)].append( ((ind + d[0], j + d[1]), 1) )
                            dist[(ind, j)] = float("inf")
                        else:
                            graph[(ind, j)].append( ((ind + d[0], j + d[1]), 0) )
                            dist[(ind, j)] = float("inf")
        
        dist[ (len(grid)-1, len(grid[0])-1)] = float('inf')
        # print(graph)
        # print(dist)

        dist[(0,0)] = 0

        priority_queue = [(0, (0, 0))]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If the popped distance is greater than the recorded one, skip (already processed)
            if current_distance > dist[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight

                # Relaxation step
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        
        # print(dist)

        return dist[ (len(grid)-1, len(grid[0])-1)]


