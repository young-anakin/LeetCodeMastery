class Solution:
    def minimumLength(self, s: str) -> int:
        dd = defaultdict(int)
        cp = 0
        for ind in s:
            dd[ind] +=1
            cp +=1
            if dd[ind] == 3:
                dd[ind] = 1
                cp -=2
        
        return cp