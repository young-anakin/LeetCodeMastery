class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dd = defaultdict(int)
        for ind in allowed:
            dd[ind] +=1
        cp = 0
        for word in words:
            cp +=1
            for ind in word:
                if ind not in dd:
                    cp -=1
                    break
        return cp