class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) == len(str2):
            if str1 != str2:
                return ""
            else:
                return str1
        

        common = ""
        word = ""
        working = ""
        if len(str1) <= len(str2):
            word = str1
        else:
            word = str2

        for ind in range(len(word)):
            common += word[ind]
            if common == str1[:ind+1] and common == str2[:ind+1]:
                if (common * int(len(str1)/len(common)) == str1) and (common * int(len(str2)/len(common)) == str2):
                    working = common
                else:
                    continue
            else:
                break
        
        return(working)