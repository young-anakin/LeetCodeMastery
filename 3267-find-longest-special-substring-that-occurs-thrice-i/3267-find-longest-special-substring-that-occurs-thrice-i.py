class Solution:
    def maximumLength(self, s: str) -> int:
        dd = defaultdict(int)
        for ind in range(1, len(s)):
            x = 0
            y = x + ind

            while y <= len(s):
                dd[s[x:y]] +=1
                x +=1
                y +=1
        mx = -1
        for key, val in dd.items():
            if val >= 3 and len(set(key)) == 1:
                # print(key, val)
                mx = max(mx, len(key))

        # print(dd)
        return mx

