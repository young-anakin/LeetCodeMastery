class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        bad = n 
        while low <= high: 
            test = (low + high)//2
            if isBadVersion(test):
                bad = test 
                high = test - 1
            else: 
                low = test + 1
        
        return bad