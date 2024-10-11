class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        mn = 0

        heap = []

        for ind, val in enumerate(times):
            heapq.heappush(heap, (val[0], val[1], ind))

        # print(heap)
        available = [ind for ind in range(len(times))]
        pos = defaultdict(int)
        last = 0
        while heap:
            val = heapq.heappop(heap)
            # print(val)
            if len(val) == 3:
                if val[2] == targetFriend:
                    # print("av", available)
                    ans = heapq.heappop(available)
                    return ans
                else:
                    tt = heapq.heappop(available)
                    pos[val[2]] = tt
                    heapq.heappush(heap, (val[1], val[2]))
            else:
                heapq.heappush(available, pos[val[1]])
        
        return 1