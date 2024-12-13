class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr = []
        heapq.heapify(arr)
        visited = set()
        for ind, val in enumerate(nums):
            heapq.heappush(arr, (val, ind))
        
        cp = 0
        while arr:
            val, ind= heapq.heappop(arr)    
            if ind not in visited:
                cp += val
            
                visited.add(ind+1)
                visited.add(ind-1)
                visited.add(ind)

        return cp
        print(arr[0])