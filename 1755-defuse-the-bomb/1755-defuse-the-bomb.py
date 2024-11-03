class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ln = len(code)
        code.extend(code)
        ans = [0 for i in range(ln)]
        if k == 0:
            return ans
        start = 0
        if k < 0:
            ans = []
            k = abs(k)
            start = ln
            for ind in range(start, start + ln):
                sm = 0
                cp = ind -1
                for j in range(k):
                    sm += code[cp]
                    cp -=1
                ans.append(sm)

        else:
            ans = []
            for ind in range(0, ln):
                sm = 0
                for j in range(1, k+1):
                    sm += code[ind + j]
                ans.append(sm)
            return ans


        return ans