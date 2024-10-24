class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cp = 0
        for word in words:
            if len(word) > len(s):
                continue
            if s[0:len(word)] == word:
                cp +=1
        
        return cp