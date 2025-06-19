class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # n = 5 -> 3 -> (n(n+1))/2

        # Output and Input binary search -> Output Binary search

        valid = 0

        def checker(md):
            naturalSum = (md * (md+1))/2

            return naturalSum <= n

        low, high = 0, n
        while low <= high:
            md = (low + high)//2
            if checker(md):
                valid = md
                low = md + 1
            else:
                high = md-1
        
        return valid
        # 0, 5
        # md = 2

        # 3, 5
        # md = 4