class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for ind in words:
            dd = defaultdict(str)
            zz = defaultdict(str)
            fl = True
            if len(ind) != len(pattern):
                continue
            else:
                for x in range(len(pattern)):
                    if not dd[pattern[x]] and not zz[ind[x]]:
                        dd[pattern[x]] = ind[x]
                        zz[ind[x]] = pattern[x]
                    
                    else:
                        if dd[pattern[x]] != ind[x] or zz[ind[x]] != pattern[x]:
                            fl = False
                            break
                if fl:
                    ans.append(ind)
        return ans