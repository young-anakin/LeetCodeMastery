class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1Dict = Counter(s1)
        s2Dict = Counter(s2)

        for key in s1Dict.keys():
            if key not in s2Dict or s2Dict[key] != s1Dict[key]:
                return False
        
        for key in s2Dict.keys():
            if key not in s1Dict or s2Dict[key] != s1Dict[key]:
                return False
        
        diff = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff +=1

        if diff == 0:
            return True
        if diff != 2:
            return False
        
        return True