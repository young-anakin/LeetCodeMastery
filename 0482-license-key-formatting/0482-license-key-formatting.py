class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        stack = []

        s = s[::-1]

        ans = ""
        cp = 0
        for ind in s:
            if ind != "-":
                stack.append(ind.upper())
                if len(stack) == k:
                    ans += "".join(stack)
                    ans += "-"
                    cp +=1
                    stack = []
        
        for ind in stack:
            ans += ind
        
        ans = ans[::-1]
        if ans and ans[0] == "-":
            return ans[1:]
        # print(ans)
        # print(stack, cp)
        return ans
                    