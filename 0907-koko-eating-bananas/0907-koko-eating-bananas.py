class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checker(k):
            cp = 0
            for ind in piles:
                cp += math.ceil(ind/k)
            if cp <= h:
                return True
            return False
        
        left = 1
        right = sum(piles)

        while left < right:
            md = (left+right)//2
            if checker(md):
                right = md
            else:
                left = md+1

        return right
