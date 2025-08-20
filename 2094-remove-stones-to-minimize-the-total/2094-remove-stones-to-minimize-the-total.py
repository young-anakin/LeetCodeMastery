class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        

        piles = [piles[i] * -1 for i in range(len(piles))]
        heapq.heapify(piles)
        while piles and k != 0:
            k -=1
            val = -1 * heapq.heappop(piles)
            val -= val//2
            heapq.heappush(piles, -1 * val)
        
        piles = [piles[i] * -1 for i in range(len(piles))]
        return (sum(piles))

            