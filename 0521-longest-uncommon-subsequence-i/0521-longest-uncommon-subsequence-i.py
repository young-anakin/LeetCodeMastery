class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        mx = -1
        for ind in range(0, min(len(a), len(b))):
            if ind < len(a) and ind < len(b):
                if a[ind] != b[ind]:
                    mx = max(mx, len(a))
                    mx = max(mx, len(b))
        
        if len(a) != len(b):
            mx = max(mx, len(a))
            mx = max(mx, len(b))
            
        return mx