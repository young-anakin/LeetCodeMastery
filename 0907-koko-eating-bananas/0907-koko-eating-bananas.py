class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # N Log N

        # K -> per hour banana we want to minimize k


        # We are trying to guess K -> Banana eating rate per hour

        def check(md):
            
            bananas = 0
            for val in piles:
                bananas += ceil(val/md)
            
            return bananas <= h

        
        low = 1
        high = sum(piles)
        valid = float('inf')
        while low <= high:
            md = (low + high)//2

            if check(md):
                valid = min(md, valid)
                high = md-1
            else:
                low = md + 1
        
        return valid

