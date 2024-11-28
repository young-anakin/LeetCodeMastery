class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ind in s:
            if len(stack) >= 2:
                if stack[-2] == "A" and stack[-1] == "B":
                    stack.pop()
                    stack.pop()
                elif stack[-2] == "C" and stack[-1] == "D":
                    stack.pop()
                    stack.pop()
            stack.append(ind)
            if len(stack) >= 2:
                if stack[-2] == "A" and stack[-1] == "B":
                    stack.pop()
                    stack.pop()
                elif stack[-2] == "C" and stack[-1] == "D":
                    stack.pop()
                    stack.pop()
        return len(stack)