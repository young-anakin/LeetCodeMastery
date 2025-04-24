class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ind in num:
            if not stack:
                stack.append(ind)
            else:
                while k != 0 and stack and ind < stack[-1]:
                    stack.pop()
                    k -=1
                stack.append(ind)
        
        while k > 0:
            k -=1
            stack.pop()
        stack = stack[::-1]
        print(stack)
        while stack and stack[-1] == '0':
            stack.pop()
        if not stack:
            return "0"
        return "".join(stack[::-1])
