class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a =  bin(start)[2:]
        b =  bin(goal)[2:]
        a = a[::-1]
        b = b[::-1]
        cp = 0
        mx = max(len(a), len(b))

        while len(a) < mx:
            a += "0"
        
        while len(b) < mx:
            b += "0"


        for ind in range(max(len(a), len(b))):
            if ind >= len(a):
                if b[ind] == 1:
                    cp +=1
            elif ind >= len(b):
                if a[ind] == 1:
                    cp +=1
            elif a[ind] == b[ind]:
                continue
            else:
                cp +=1
        # print(a, b)
        return cp