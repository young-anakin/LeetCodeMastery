class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        cp = 0
        dir = True
        while cp < time:
            if i == n:
                dir = False
            if i == 1:
                dir = True
            
            if dir:
                i +=1
            else:
                i -=1
            cp +=1
        
        return i