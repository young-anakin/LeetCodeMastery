class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        stack = []

        for ind in arr:
            if ind %2 == 0:
                stack = []
            else:
                stack.append(ind)
                if len(stack) == 3:
                    return True
        return False