class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        a, b, c, d = 0,0,0,0

        a = int(event1[0][0:2]) * 60 + int(event1[0][3:])
        b = int(event1[1][0:2]) * 60 + int(event1[1][3:])
        c = int(event2[0][0:2]) * 60 + int(event2[0][3:])
        d = int(event2[1][0:2]) * 60 + int(event2[1][3:])

        if (a < c and b < c and a < d and b < d) or (a > c and b > c and a > d and b > d):
            return False
        
        return True
        print(a, b, c, d)