class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        stack = 0

        for ind in arr:
            if ind %2 == 0:
                stack = 0
            else:
                stack +=1
                if stack == 3:
                    return True
        return False