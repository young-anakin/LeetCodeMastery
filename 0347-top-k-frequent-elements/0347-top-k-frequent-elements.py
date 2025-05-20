class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = Counter(nums)

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        ans = []
        print(heap)
        while k != 0:
            k -=1
            ans.append(heapq.heappop(heap)[1])
        
        return ans