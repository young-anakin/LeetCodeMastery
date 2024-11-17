class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        mxLength = float("inf")
        currSum = 0
        heap = []
        for ind in range(len(nums)):
            currSum += nums[ind]
            # print(currSum)
            # print(currSum)
            if currSum >= k:
                # print(ind, currSum)
                # print(heap)
                mxLength = min(mxLength, ind+1)
            while heap:
                if heap:
                    if currSum - heap[0][0] >= k:
                        # currSum -= heap[-1][0]
                        mxLength = min(mxLength, abs(ind - heap[0][1]))
                        heapq.heappop(heap)
                    else:
                        break
                else:
                    break
                # mxLength = min
                
                
            heapq.heappush(heap, (currSum, ind))
        
        if mxLength == float("inf"):
            return -1
        return mxLength