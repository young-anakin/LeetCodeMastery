class Solution:
    def myAtoi(self, s: str) -> int:
        mx = pow(2,31) -1
        mn = -1 * (pow(2,31)) 
        available  = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        leading = False
        neg = False
        lastZero = True
        ans = []
        read = False
        for ind in s:
            if ind not in available or (lastZero == True and ind == "0"):
                if ind == "-" and not read:
                    neg = True
                    read = True
                    continue

                if ind == "+" and not read:
                    neg = False
                    read = True
                    continue
                
                elif lastZero == True and (ind == "0" or ind == " "):
                    if ind == "0":
                        read = True
                    if read == True and ind == " ":
                        break
                    continue
                
                else:
                    break
            else:
                ans.append(ind)
                read = True
                lastZero = False
        if len(ans) == 0:
            return 0
        if neg:
            if -1 * int("".join(ans)) < mn:
                return mn
            return -1 * int("".join(ans))
        if int("".join(ans)) > mx:
            return mx
        return int("".join(ans))


                