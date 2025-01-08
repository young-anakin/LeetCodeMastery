class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cp = 0
        for ind in range(len(words)):
            for j in range(ind +1, len(words)):
                if ind == j:
                    continue
                if words[j][0:len(words[ind])] == words[ind] and words[j][-len(words[ind]):] == words[ind]:
                    cp +=1
        
        return cp