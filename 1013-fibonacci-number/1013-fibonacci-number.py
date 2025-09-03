class Solution:
    def fib(self, n: int) -> int:
        
        memo = defaultdict(int)

        def rec(n):
            if n == 0 or n == 1:
                return n
            
            if n not in memo:
                memo[n] = rec(n-1) + rec(n-2)

            return memo[n]
        
        return rec(n)