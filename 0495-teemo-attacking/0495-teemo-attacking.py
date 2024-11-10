class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        curr = 0
        prev = 0
        for ind in timeSeries:
            
            curr = ind + duration
            ans += duration

            if ind < prev:
                ans -= abs(ind-prev)
            # print(prev, curr)
            prev = curr
        
        return ans