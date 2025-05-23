class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # [1, 2, 1]
        # 2, -1, 2

        # 2, -1, 2
        # [1, 2, 1, 1, 2, 1]
        # [(2, 1), (2, 4), (1, 5)] -True
        #

        stack = list()
        
        sub = [ind for ind in nums]
        sub.extend(nums)
        mn = [-1] * len(nums)
        print(sub)
        # print(mn)
        for ind in range(len(sub)):
            if not stack:
                stack.append((sub[ind], ind))
            else:
                while stack and stack[-1][0] < sub[ind]:
                    val, i = stack.pop()
                    if i < len(mn):
                        mn[i] = sub[ind]
                        # stack.append((sub[ind], ind))
                else:
                    stack.append((sub[ind], ind))
            # print(stack)
        return mn