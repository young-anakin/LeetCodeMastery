class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ind in range(len(s)):
            stack.append(s[ind])
            if len(stack) >= 3:
                if stack[-1] == stack[-2] == stack[-3]:
                    stack.pop()
        
        return "".join(stack)