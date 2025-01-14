class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heap = list()
        heapq.heapify(heap)

        minHeap = list()
        heapq.heapify(minHeap)

        for ind in range(n):
            heapq.heappush(heap, ind)
        
        meetings.sort()
        ind = 0

        dd = defaultdict(int)
        print(meetings)
        print(heap)
        for ind in meetings:
            while minHeap and ind[0] >= minHeap[0][0]:
                y, x = heapq.heappop(minHeap)
                heapq.heappush(heap, x)
            if heap:
                val = heapq.heappop(heap)
                dd[val] +=1
                heapq.heappush(minHeap, (ind[1], val))
            else:
                x, val = heapq.heappop(minHeap)
                dd[val] +=1       
                heapq.heappush(minHeap, (x + abs(ind[0] - ind[1]), val))
            # print(heap, minHeap)

        mx = max(dd.values())
        print(mx)
        for ind in range(n):
            if dd[ind] == mx:
                return ind
