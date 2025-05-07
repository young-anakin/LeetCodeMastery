class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        sub = ""
        mx = 0
        ans = ""
        for i in range(len(str2)):
            sub += str2[i]
            if sub * (len(str1)//len(sub)) == str1 and sub * (len(str2)//len(sub)) ==  str2:
                if len(sub) > mx:
                    mx = len(sub)
                    ans = sub

        sub = ""
        for i in range(len(str1)):
            sub += str1[i]
            if sub * (len(str1)//len(sub)) == str1 and sub * (len(str2)//len(sub)) ==  str2:
                if len(sub) > mx:
                    mx = len(sub)
                    ans = sub
        
        return ans
            
            

        