class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = "0123456789"
        for ind in s:
            if ind in digits:
                if stack:
                    stack.pop()
                # stack.append(ind)
            else:
                stack.append(ind)
        
        return "".join(stack)

