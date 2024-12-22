class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dd = defaultdict(int)
        
        if len(s) == 0:
            return 0
        i = 0
        mx = 0
        for x, ind in enumerate(s):
            dd[ind] +=1
            while dd[ind] != 1:
                dd[s[i]] -=1
                i +=1
            
            mx = max(mx, abs(x - i))
        
        return mx+1
            
                