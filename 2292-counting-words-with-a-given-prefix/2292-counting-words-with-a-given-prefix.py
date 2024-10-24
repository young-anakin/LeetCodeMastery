class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cp = 0
        for word in words:
            if word[0:len(pref)] == pref:
                cp +=1
        
        return cp