class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        m = n
        n = abs(n)
        # x = abs(x)
        
        def rec(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                tmp = rec(x, n//2)
                return tmp * tmp
            else:
                tmp = rec(x, n//2)
                return x * tmp * tmp
        
        if m < 0:
            return 1/rec(x, n)
        return rec(x, n)