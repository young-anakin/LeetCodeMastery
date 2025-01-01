class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dd = defaultdict(int)

        ss = set()

        for ind in s:
            ss.add(ind)
        
        cp = Counter(t)
        i, j = 0, 0
        need, have = len(t), 0
        
        mx = float("inf")
        x, y = 0, 0
        while j < len(s):
            if s[j] in ss:
                if dd[s[j]] < cp[s[j]]:
                    have +=1
                dd[s[j]] +=1
            j +=1
            while have == need:
                if j - i < mx:
                    mx = min(mx, j - i)
                    x, y = i, j

                if s[i] in ss:
                    dd[s[i]] -=1
                    if dd[s[i]] < cp[s[i]]:
                        have -=1
                        i +=1
                        break
                i +=1

            
    
        print(x, y)

        return s[x:y]

            # s[i]