# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1

        right = n

        while left <= right:
            md = (left + right)//2

            val = isBadVersion(md)

            print(md)
            if val == True:
                if isBadVersion(md-1) == False:
                    return md
                else:
                    right = md -1
            else:
                left = md + 1
