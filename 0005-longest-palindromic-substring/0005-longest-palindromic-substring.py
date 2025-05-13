class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxStr = ""
        mxLen = 0

        for i in range(len(s)):

            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right-left + 1) >= mxLen:
                    mxLen = max(mxLen, abs(right-left+1))
                    mxStr = s[left:right+1]
                left, right = left - 1, right + 1


            left, right = i, i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if (right-left+ 1) >= mxLen:
                    mxLen = max(mxLen, abs(right-left+1))
                    mxStr = s[left:right+1]
                left, right = left - 1, right + 1
        
        return mxStr
            
