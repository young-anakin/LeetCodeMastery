class Solution:
    def isNumber(self, s: str) -> bool:
        exponent = False
        sign = False
        dot = False
        digit = False

        stack = []

        for ind in range(len(s)):
            if s[ind] == "-" or s[ind] == "+":
                if ind == len(s)-1:
                    return False
                if exponent or digit or dot or sign:
                    # print(stack)
                    if len(stack) > 0 and (stack[-1] == "E" or stack[-1] == "e"):
                        # stack.append(s[ind])
                        pass
                    else:
                        # print(sign, exponent, digit, dot)

                        # print("m")
                        return False
                    
                    if ind == len(s)-1:
                        # print("mn")

                        return False
                
                stack.append(s[ind])
                sign = True
            
            elif s[ind] == ".":
                if not digit and ind == len(s)-1:
                    return False
                if exponent or dot:
                    return False
                stack.append(s[ind])
                dot = True
            
            elif s[ind] == "e" or s[ind] == "E":
                if ind == len(s)-1:
                    return False
                if exponent:
                    return False
                if not digit:
                    return False
                stack.append("E")
                exponent = True
            elif s[ind] == "0" or s[ind] == "1" or s[ind] == "2" or s[ind] == "3" or s[ind] == "4" or s[ind] == "5" or s[ind] == "6" or s[ind] == "7" or s[ind] == "8" or s[ind] == "9":
                digit = True
                stack.append(int(s[ind]))
            else:
                return False

        return True