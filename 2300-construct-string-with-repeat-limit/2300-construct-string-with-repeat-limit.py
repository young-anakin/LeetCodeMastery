class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ss = list(set(s))

        ans = [ind for ind in ss]
        dd = Counter(s)
        
        heap = []
        heapq.heapify(heap)
        ans.sort(reverse = True)
        cp = 0
        for val in ans:
            heapq.heappush(heap, (cp, val, dd[val]))
            cp +=1
        print(heap)
        fin = ""
        counter = 0
        while heap:
            a, b, c = heapq.heappop(heap)
            tmp = 0
            print(a, b, c)
            if c < 0:
                print(a,b,c)
                continue
            for ind in range(c):
                if tmp != 0 and tmp % repeatLimit == 0:
                    x = "0"
                    while heap and heap[0][2] <= 0:
                        heapq.heappop(heap)
                    if len(heap) <= 0:
                        break
                    else:
                        x, y, z = heapq.heappop(heap)
                        fin += y
                        heapq.heappush(heap, (x, y, z-1))
                    tmp = 0
                    fin += b
                else:
                    fin += b
                tmp += 1
        return fin



