class Solution:
    def fractionAddition(self, expression: str) -> str:
        values = []

        stack = []

        for ind in expression:
            if stack and (ind == "-" or ind == "+"):
                val = "".join(stack)
                values.append(val)
                stack = []
            stack.append(ind)
        
        if stack:
            val = "".join(stack)
            values.append(val)
        
        ans = []
        for ind in values:
            if ind[0] == "+" or ind[0] == "-":
                ans.append(ind)
            else:
                ans.append("+" + ind)
        # print(values)
        ans  = ans[::-1]
        while len(ans) > 1:
            a = ans.pop()
            b = ans.pop()
            print(a, b)
            if a[a.index("/") + 1: ] == b[b.index("/")+1: ]:
                val = int(a[0:a.index("/")]) + int(b[0:b.index("/")])
                if val == 0:
                    ans.append("+0/1")
                else:
                    num, denom = int(val), int(a[a.index("/")+1:])
                    while gcd(num, denom) != 1:
                        tt = gcd(num, denom)
                        num //= tt
                        denom //= tt
                    if str(num)[0] == '-':
                        tmp =  str(num) + "/" + str(denom)
                    else:
                        tmp = "+" + str(num) + "/" + str(denom)
                    ans.append(tmp)
            else:
                # print("ya")
                val = (int(a[0:a.index("/")]) * int(b[b.index("/") + 1 : ])) + (int(a[a.index("/")+1:]) * int(b[0:b.index("/")]))
                bottom = int(a[a.index("/")+1:]) * int(b[b.index("/")+1:])
                # print(a[0:2], b)
                # print(int(a[0:2]) * int(b[-1])), (int(a[-1]) * int(b[0:2]))
                # if gcd()
                while gcd(val, bottom) != 1:
                    gg = gcd(val, bottom)
                    print("y0ooo", val, bottom)
                    val //= gg
                    bottom = bottom//gg
                    # print("ha", val, bottom)
                if str(val)[0] == '-':
                    tmp =  str(val) + "/" + str(bottom)
                else:
                    tmp = "+" + str(val) + "/" + str(bottom)
                ans.append(tmp)   

        # print(values)

        if ans[0][0] == "-":
            return ans[0]
        else:
            return ans[0][1:]
        print(ans)
        # print(ans)