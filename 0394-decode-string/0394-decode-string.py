class Solution:
    def decodeString(self, s: str) -> str:
        # if s == "3[a]2[bc]":
        #     return "jjo"
        stack = []
        fin = ""
        nums = "1234567890"
        for i in range(len(s)):
            if s[i] == "[":
                # print(i, s[i])
                stack.append(s[i])
            elif s[i] == "]":
                # print("orig", stack)
                repeat = []
                value = []
                while stack[-1] != "[":
                    value.append(stack.pop())
                    # stack.pop()
                value = value[::-1]
                stack.pop()
                print(stack)
                while stack and stack[-1] in nums:
                    repeat.append(stack.pop())
                repeat = repeat[::-1]

                # print("Repeat and val", repeat, value)
                repeat = "".join(repeat)
                for x in range(int(repeat)):
                    stack.append("".join(value))
                # print("changed", stack)
                # for x in tmp:
                #     stack.append(x)
            else:
                stack.append(s[i])
        return "".join(stack)
        # print(stack)