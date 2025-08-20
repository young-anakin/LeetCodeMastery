class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-1 * nums[i] for i in range(len(nums))]

        heapq.heapify(nums)
        while nums:
            val = heapq.heappop(nums)
            k -=1
            if k == 0:
                return -1 * val