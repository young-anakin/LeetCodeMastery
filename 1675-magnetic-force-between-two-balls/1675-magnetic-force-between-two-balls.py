class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(x, m):
            prevBall = position[0]

            placed =1

            for i in range(1, len(position)):
                curBall = position[i]

                if curBall - prevBall >= x:
                    placed +=1
                    prevBall = curBall
                
                if placed == m:
                    return True
            
            return False
        

        ans = 0

        low = 1
        high = int(position[-1]/ (m-1.0)) + 1

        while low <= high:
            md = low + (high - low)//2

            if check(md, m):
                ans = md
                low = md + 1
            
            else:
                high = md - 1
        
        return ans
        