class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        dd = defaultdict(str)
        s = 97
        for ind in range(25):
            dd[chr(s)] = chr(s+1)
            s +=1
        
        dd['z'] = 'a'
        # print(dd)
        if len(str2) > len(str1):
            return False

        one = 0
        cp = 0
        found = 0
        for ind in str2:
            if one < len(str1) and (ind == str1[one] or dd[str1[one]] == ind):
                one +=1
                cp +=1
                found +=1 
            else:
                while True:
                    if one >= len(str1):
                        break
                    if one < len(str1) and (str1[one] != ind and dd[str1[one]] != ind):
                        one +=1
                        # print("yaaa", ind)
                    else:
                        found +=1
                        one +=1 
                        break
        # print(found)
            
        if found != len(str2):
            return False
        return True
        # print(ord('a'))