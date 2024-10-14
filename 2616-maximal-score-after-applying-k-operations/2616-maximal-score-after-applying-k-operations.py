class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for ind in nums:
            heapq.heappush(heap, -1 * ind)

        ans = 0
        # print(heap)
        while heap and k > 0:
            val = heapq.heappop(heap)

            ans += -1 * val
            heapq.heappush(heap, math.floor(val/3))
            k -=1 
            # print(heap, ans)
        
        return ans