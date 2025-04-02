class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # This dictionary will store letterCounts for me

        letterCount = defaultdict(int)


        # Approach : I'll iterate over the string adding letter by letter into my dictionary. If I encounter a character that has a value more than 1, then that's the longest substring I've reached so far. I'll have to decrement from the start of my string upto which that letter becomes 1. 

        standBy, leader = 0, 0
        finishLine = len(s)
        maxSubStr = 0
        while leader < finishLine:

            letterCount[s[leader]] +=1

            while letterCount[s[leader]] > 1:
                letterCount[s[standBy]] -=1
                standBy +=1
            
            # maximum sub string is going to be the distance between the leader and the stand by guy
            leader +=1
            # print(standBy, leader, maxSubStr)
            maxSubStr = max(maxSubStr, abs(standBy - leader))
        
        return maxSubStr