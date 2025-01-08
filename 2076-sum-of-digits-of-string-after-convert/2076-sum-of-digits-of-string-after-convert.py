class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tot = []
        for val in s:
            x = str(ord(val) - 96)
            for i in x:
                tot.append(i)

        print(tot)
        while k != 0:
            ans = str(sum(map(int, tot)))
            sub = []
            for i in ans:
                sub.append(i)
            tot = sub
            k -=1
        fin = ""
        for ind in tot:
            fin += ind
    
        return int(fin)