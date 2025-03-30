class Solution:
    def firstUniqChar(self, s: str) -> int:
        cp = Counter(s)
        for x, i in enumerate(s):
            if cp[i] == 1:
                return x
        
        return -1