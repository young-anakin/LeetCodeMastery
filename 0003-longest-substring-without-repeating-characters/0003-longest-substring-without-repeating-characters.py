class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dd = defaultdict(int)
        arr = []
        l = 0
        r = 0
        mx = -1
        # cp = 0
        while r < len(s):
            if dd[s[r]] == 0:
                dd[s[r]] +=1
                r +=1
            else:
                while dd[s[r]] != 0:
                    dd[s[l]] -=1
                    l +=1
                
                dd[s[r]] +=1
                r+=1
            
            mx = max(mx, abs(r-l))
        
        mx = max(mx, abs(r-l))

        return mx
