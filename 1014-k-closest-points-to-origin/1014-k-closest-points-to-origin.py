class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []

        for a, b in points:
            ans.append((math.sqrt((a)**2  + (b)**2), [a, b])) 

        
        heapq.heapify(ans)
        fin = []
        for i in range(k):
            fin.append(heapq.heappop(ans)[1])
        
        return fin

                
        