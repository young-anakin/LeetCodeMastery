class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = set()

        group_heap = []
        tot = []

        heap = []
        i = 0
        for a, b in intervals:
            heapq.heappush(heap, (a,b) )

        while heap:
            a, b = heapq.heappop(heap)
            if b != float("inf"):
                heapq.heappush(heap, (b, float('inf')))
                if len(group_heap) == 0:
                    groups.add(i)
                    i +=1
                else:
                    heapq.heappop(group_heap)
            else:
                heapq.heappush(group_heap, 0)
        return len(groups)
