class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ind in s:
            if stack:
                if stack[-1] == "(" and ind == ")":
                    stack.pop()
                else:
                    stack.append(ind)
            else:
                stack.append(ind)
        
        print(stack)
        return len(stack)
