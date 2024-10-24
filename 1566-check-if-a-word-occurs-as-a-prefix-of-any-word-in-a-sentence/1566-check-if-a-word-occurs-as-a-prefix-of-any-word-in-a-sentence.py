class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(" ")
        for ind, word in enumerate(arr):
            # print(word)
            if len(word) < len(searchWord):
                continue
            else:
                if word[0:len(searchWord)] == searchWord:
                    return ind+1
        
        return -1