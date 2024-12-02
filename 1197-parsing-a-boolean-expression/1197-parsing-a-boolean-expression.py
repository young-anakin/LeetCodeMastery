class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ans = False
        x = expression[::-1]
        stack = []
        for ind in range(len(expression)):
            if x[ind] == ",":
                continue
            if x[ind] == ")" or x[ind] == "(":
                stack.append(x[ind])
            elif x[ind] == "f" or x[ind] == "t":
                if x[ind] == "t":
                    ans = True
                stack.append(x[ind])
            else:
                openCp = 0
                closeCp = 0
                arr = []
                # if x[ind] == "|":
                # print(stack, x[ind])
                while openCp != 1 or closeCp != 1:
                    t = stack.pop()
                    if t == "(":
                        openCp +=1
                    elif t == ")":
                        closeCp +=1
                    else:
                        arr.append(t)
                    # print(t)
                if x[ind] == "|":
                    if len(arr) == 0:
                        ans = ans
                    else:
                        if "t" in arr:
                            ans = True
                        else:
                            ans = False
                elif x[ind] == "&":
                    if len(arr) == 0:
                        ans = ans
                    else:
                        if "f" in arr:
                            ans = False
                        else:
                            ans = True
                elif x[ind] == "!":
                    if ans == True:
                        ans = False
                    else:
                        ans = True
                
                # print(stack, ans)
                if ans == True:
                    stack.append("t")
                else:
                    stack.append("f")
                # print("Agew", arr, x[ind], ans, stack)
                

                    

        return ans
        print(x)