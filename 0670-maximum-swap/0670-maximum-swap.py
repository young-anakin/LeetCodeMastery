class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = []
        ss = str(num)
        for val, ind in enumerate(ss):
            heapq.heappush(ans, (int(ind) * -1, -1 * val))
            # ans.append(int(ind))
        
        # ans.sort(reverse = True)
        swap = False
        val = []
        cp = Counter(ss)
        swapped, index = 0,0
        print(ans[0])
        for ind in ss:
            if not(swap) and int(ind) == -1 * ans[0][0]:
                cp[ind] -=1
                if cp[ind] == 0:
                    while ans and ans[0][0] ==  -1 * int(ind):
                        heapq.heappop(ans)
                    # print(ans[0], int(ind))
                    # print("largestttt", ans[0])
                
                val += ind
                # print("hey", cp, ans[0])
                # pass
            else:
                if ans and not(swap) and int(ind) < -1 * ans[0][0]:
                    print("Yo", ind)
                    val += str(-1 * ans[0][0])
                    swap = True
                    swapped, index = ind, -1 * ans[0][1]
                    continue
                else:
                    val += str(ind)
            print(val)

            # val += str(ind)
        print(swapped, index)
        if (swap):
            val[index] = swapped
        print("fin", val)
        return int("".join(val))