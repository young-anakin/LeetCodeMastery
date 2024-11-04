class Solution:
    def compressedString(self, word: str) -> str:
        output = []
        ans = ""
        output.append(word[0])
        cp = 1
        for ind in range(1, len(word)):
            if not output:
                output.append(word[ind])
            if output and output[-1] == word[ind]:
                if len(output) == 9:
                    ans += str(len(output))
                    ans += word[ind]
                    output = []
                    output.append(word[ind])
                else:
                    output.append(word[ind])
            else:
                ans += str(len(output))
                ans += output[-1]
                output = []
                output.append(word[ind])
        
        if output:
            ans += str(len(output))
            ans += output[-1]
        
        return ans

