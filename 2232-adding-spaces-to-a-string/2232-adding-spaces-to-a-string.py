class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        k = 0
        for ind, val in enumerate(s):
            if k < len(spaces) and ind == spaces[k]:
                ans += " "
                k +=1
            ans += val
            # print(ans)
        return ans