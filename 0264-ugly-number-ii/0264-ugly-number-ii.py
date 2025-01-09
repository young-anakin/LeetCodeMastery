class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        cp = 0

        visited = set()
        while cp < n:
            cp +=1
            val  = heapq.heappop(heap)
            # if cp == n+1:
            #     return val
            
            if 2 * val not in visited:
                heapq.heappush(heap, 2*val)
                visited.add(2*val)
            if 3 * val not in visited:
                heapq.heappush(heap, 3*val)
                visited.add(3*val)
            
            if 5 * val not in visited:
                heapq.heappush(heap, 5*val)
                visited.add(5*val)
        
        print(heap)
        return val
        
