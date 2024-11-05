class Solution:
    def minChanges(self, s: str) -> int:
        cp = 0
        for ind in range(len(s)):
            if ind%2 == 1:
                if s[ind] != s[ind-1]:
                    cp +=1
        return cp


