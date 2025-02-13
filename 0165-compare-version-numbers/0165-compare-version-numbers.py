class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        first = version1.split(".")
        second = version2.split(".")
        a, b = 0, min(len(first), len(second))
        for i in range(b):
            if int(first[i]) > int(second[i]):
                return 1
            elif int(first[i]) < int(second[i]):
                return -1
            a +=1
        
        while len(first) > a:
            if int(first[a]) > 0:
                return 1
            a +=1
        while len(second) > a:
            if int(second[a]) > 0:
                return -1
            a +=1
        return 0