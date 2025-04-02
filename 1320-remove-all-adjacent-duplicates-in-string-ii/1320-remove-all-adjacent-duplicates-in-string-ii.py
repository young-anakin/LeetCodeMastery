class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # I'll use a tuple based stack that tracks each element with how many times it has appeared. If it happens to have the same value as the previous element, we merge them together and increase their count!


        stack = []
        i = 0


        for i in range(len(s)):
            if not stack:
                stack.append((s[i], 1))
            else:
                if stack[-1][0] == s[i]:
                    x, y = stack.pop()
                    stack.append((x, y + 1))
                else:
                    stack.append((s[i], 1))
            
            if stack[-1][1] == k:
                stack.pop()
        
        # print(stack)

        ans = ""
        for key, val in stack:
            ans += key * val
        
        return ans