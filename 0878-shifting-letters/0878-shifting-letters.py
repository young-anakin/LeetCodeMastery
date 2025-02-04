class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        suffix = [0]
        pp = shifts[::-1]
        for ind in range(len(pp)):
            suffix.append(suffix[-1] + pp[ind])
        
        suffix = suffix[1:]
        suffix = suffix[::-1]
        fin = []
        for ind in suffix:
            fin.append(ind % 26)
        
        ans = ""
        for ind, val in enumerate(s):
            x = ord(val) + fin[ind] 
            if x > 122:
                x = 97 + abs(122 - x) -1
            ans += chr(x)
        

        print(fin)
        print(ord('a'))
        return ans
        # print(suffix)