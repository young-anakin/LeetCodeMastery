class Solution:
    def climbStairs(self, n: int) -> int:
        
        # either in 1 step or 2 steps
        memo = defaultdict(int)
        def dp(i):
            # base case
            if i == n:
                return 1
            
            if i > n:
                return 0
            if i not in memo:
                memo[i] = dp(i + 1) + dp(i + 2)
            return memo[i]
        
        return dp(0)
        
        # dp(1) + dp(2)
        # dp(2) + dp(3)

