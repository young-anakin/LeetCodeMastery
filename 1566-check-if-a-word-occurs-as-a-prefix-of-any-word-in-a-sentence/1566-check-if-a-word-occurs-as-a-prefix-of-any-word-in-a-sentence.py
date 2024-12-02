class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for ind, word in enumerate(words):
            if word[0:len(searchWord)] == searchWord:
                return ind+1
        
        return -1
        print(words)