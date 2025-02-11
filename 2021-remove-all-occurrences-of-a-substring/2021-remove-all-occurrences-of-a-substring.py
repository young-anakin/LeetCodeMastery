class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for i in s:
            stack.append(i)
            while len(stack) >= len(part) and "".join(stack[-len(part):]) == part:
                stack = stack[:-len(part)]
        
        return "".join(stack)