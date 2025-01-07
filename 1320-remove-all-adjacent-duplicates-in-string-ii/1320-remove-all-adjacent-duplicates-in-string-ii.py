class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ind in s:
            if not stack:
                stack.append((ind, 1))
            else:
                if stack[-1][0] == ind:
                    a, b = stack.pop()
                    stack.append((a, b+1))
                else:
                    stack.append((ind, 1))
            
            if stack[-1][1] == k:
                stack.pop()

        
        ans = ""
        for a, b in stack:
            ans += a*b
        return ans