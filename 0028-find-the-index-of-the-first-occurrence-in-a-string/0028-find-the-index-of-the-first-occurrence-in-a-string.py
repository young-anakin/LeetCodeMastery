class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for ind in range(len(haystack)):
                fl = True
                for j in range(len(needle)):
                    if ind + j >= len(haystack):
                        continue
                    if haystack[ind + j] == needle[j]:
                        continue
                    else:
                        fl = False
                if fl:
                    return ind

        
        return -1