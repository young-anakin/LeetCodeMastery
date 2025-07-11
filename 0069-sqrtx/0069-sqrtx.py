class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        res=0
        while l<=r:
            m= (l + r)//2
            if m**2>x:
                r=m-1
            elif m**2<x:
                l=m+1
                res=m
            #if == m
            else:
                return m
        return res