class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        arr = []
        for ind in range(len(nums)):
            heapq.heappush(arr, (abs(x-nums[ind]), ind))
        ans = []
        while k:
            k -=1
            ans.append(nums[heapq.heappop(arr)[1]])
        ans.sort()
        return ans