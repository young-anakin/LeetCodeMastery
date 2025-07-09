class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        # we want to choose k bananas/hour 

        def bananaPerHour(k):
            bph = 0

            for val in piles:
                bph += math.ceil(val/k)

            return bph <= h
        
        ans = 0
        def binarySearch(low, high):
            nonlocal ans
            while low <= high:
                md = (low + high)//2

                # if valid
                if bananaPerHour(md):
                    ans = md
                    high = md - 1
                else:
                    low = md + 1
        
        binarySearch(1, sum(piles))
        return ans
        
# O(NlogN)