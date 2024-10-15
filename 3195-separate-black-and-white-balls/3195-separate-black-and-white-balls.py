class Solution:
    def minimumSteps(self, s: str) -> int:
        s = s[::-1]
        stack = []
        cp = 0
        for ind in s:
            if ind == "0":
                stack.append(0)
            else:
                cp += len(stack)
        return cp