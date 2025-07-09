# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        

        def binarySearch(left, right):

            while left < right:
                md = (left + right)//2

                if isBadVersion(md):
                    right = md
                else:
                    left = md + 1
            return left
        
        return binarySearch(1, n)