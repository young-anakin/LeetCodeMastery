class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = []
        for ind in nums:
            heapq.heappush(new, -1 * ind)
        

        i = 0
        last = -1
        while new:
            val = heapq.heappop(new)
            # if last != val:
            #     i +=1
            i +=1
            if i == k:
                return -1 * val
            last = val
            
        