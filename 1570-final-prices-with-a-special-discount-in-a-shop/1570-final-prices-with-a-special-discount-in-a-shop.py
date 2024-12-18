class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for ind in range(len(prices)):
            fl = False
            for j in range(ind+1, len(prices)):

                if prices[ind] >= prices[j]:
                    ans.append(abs(prices[ind] - prices[j]))
                    fl = True
                    break
            if not fl:
                ans.append(prices[ind])

        return ans