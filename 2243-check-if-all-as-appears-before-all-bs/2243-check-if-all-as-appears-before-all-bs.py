class Solution:
    def checkString(self, s: str) -> bool:
        a = False
        b = False
        for ind in s:
            if ind == "a":
                if b == True:
                    return False

                a = True
            else:

                b = True
                continue
        return True