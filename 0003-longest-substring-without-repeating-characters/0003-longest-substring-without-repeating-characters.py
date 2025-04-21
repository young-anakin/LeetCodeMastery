class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        # count the amount of characters
        counter = defaultdict(int)


        i = 0
        j = 0
        mx = 0
        while i < len(s):
            counter[s[i]] +=1

            while counter[s[i]] > 1:
                counter[s[j]] -=1
                j +=1
            
            mx = max(mx, abs(i-j))
            i +=1
        
        return mx+1
