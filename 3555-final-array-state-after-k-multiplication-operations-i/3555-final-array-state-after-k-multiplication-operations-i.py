class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = list()
        heapq.heapify(ans)
        for ind, val in enumerate(nums):
            heapq.heappush(ans, (val, ind))
        
        for ind in range(k):
            val, ind = heapq.heappop(ans)
            heapq.heappush(ans, (val * multiplier, ind))
        

        fin = [0 for _ in range(len(nums))]

        for a, b in ans:
            fin[b] = a
        
        return fin