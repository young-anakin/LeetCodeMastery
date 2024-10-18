class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        available  = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        last = 0
        visited = set()
        for ind in range(len(s)):
            if ind in visited:
                continue
            if s[ind] in available:
                tmp = ""
                a = ind
                while a < len(s) and s[a] in available:
                    tmp += s[a]
                    visited.add(a)
                    a +=1
                if int(tmp) > last:
                    last = int(tmp)
                else:
                    print(last, int(tmp))
                    return False
            
        
        if s[-1] not in available:
            return True
       
        return True
