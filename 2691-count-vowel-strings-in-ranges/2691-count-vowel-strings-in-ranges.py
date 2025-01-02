class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ('a', 'e', 'i', 'o', 'u')
        vowelSum = [0]
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                vowelSum.append(vowelSum[-1] + 1)
            else:
                vowelSum.append(vowelSum[-1])
        
        ans = []
        for a, b in queries:
            ans.append(vowelSum[b+1] - vowelSum[a])
        vowelSum = vowelSum[1:]
        # print(vowelSum)
        return ans