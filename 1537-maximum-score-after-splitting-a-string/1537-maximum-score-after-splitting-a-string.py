class Solution:
    def maxScore(self, s: str) -> int:
        # Approach : We calculate prefix sum for number of 0's initially and then we calculate prefix difference for 1 by initially counting the number of 1's and decreasing if we find 1. 
        
        #count number of 1's
        ones = 0
        # we subtract 1 because we have curated both the arrays so that they both account for the last member when needed. 
        n = len(s)-1
        for ind in range(len(s)):
            if s[ind] == "1":
                ones +=1
        
        #calculate the prefix difference for 1 
        onePrefix = []
        for ind in range(len(s)-1):
            if s[ind] == "1":
                ones -=1
            onePrefix.append(ones)
        
        #calculate the prefix for zeroes
        zeroCount = 0
        zeroPrefix = []
        for ind in range(len(s)-1):
            if s[ind] == "0":
                zeroCount +=1
            zeroPrefix.append(zeroCount)
        
        ans = 0
        for ind in range(len(s)-1):
            ans = max(ans, zeroPrefix[ind] + onePrefix[ind])
        return ans
        