class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        cp = Counter(nums)
        for key, val in cp.items():
            heapq.heappush(heap, (-val, key))
        
        ans = []
        while k != 0:
            ans.append(heapq.heappop(heap)[1])
            k -=1
        
        return ans