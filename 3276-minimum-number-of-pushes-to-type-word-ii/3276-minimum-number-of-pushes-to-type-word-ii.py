class Solution:
    def minimumPushes(self, word: str) -> int:
        dd = defaultdict(int)
        for ind in word:
            dd[ind] +=1
        heap = []
        for key, val in dd.items():
            heapq.heappush(heap, (-1 * val, key))
        
        turn = 1
        allowed = 2
        tot = 0

        while heap:
            a, b = heapq.heappop(heap)
            print(a,b)
            print("turn", turn, allowed)
            tot += (turn * (-1*a))
            allowed +=1

            if allowed == 10:
                turn +=1
                allowed = 2
        
        return tot
        print(heap)