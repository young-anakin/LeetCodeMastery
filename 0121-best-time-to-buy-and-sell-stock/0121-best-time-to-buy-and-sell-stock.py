class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans =  0

        stack = []
        mn = float("inf")
        for i in prices:
            if i > mn:
                ans = max(ans, abs(i - mn))
            
            else:
                mn = i
        
        return ans