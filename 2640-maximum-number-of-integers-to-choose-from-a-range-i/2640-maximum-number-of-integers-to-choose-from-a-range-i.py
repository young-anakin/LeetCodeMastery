class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ss = set(banned)
        sm = 0
        cp = 0
        for ind in range(1, n+1):
            if ind not in ss:
                # print(ind)
                sm += ind
                cp +=1
            
            if sm > maxSum:
                cp -=1
                break
        
        return cp
