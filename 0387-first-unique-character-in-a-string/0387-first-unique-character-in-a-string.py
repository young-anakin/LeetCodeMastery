class Solution:
    def firstUniqChar(self, s: str) -> int:
        dd = defaultdict(int)
        for ind in s:
            dd[ind] +=1
        
        for ind, val in enumerate(s):
            if dd[val] == 1:
                return ind

        return -1