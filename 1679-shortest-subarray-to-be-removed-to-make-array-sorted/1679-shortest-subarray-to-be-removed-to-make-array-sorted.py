class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        prefix = []
        suffix = []

        stack = []
        stack.append(arr[0])
        start = 1
        mn = 1
        beg = stack

        while start < len(arr):
            if arr[start] >= stack[-1]:
                stack.append(arr[start])
                if mn <= len(stack):
                    mn = max(mn, len(stack))

                    beg = stack
            else:
                break
            start +=1
        
        suf = [arr[-1]]

        start = 2

        while start <= len(arr):
            if arr[-start] <= suf[-1]:
                suf.append(arr[-start])  
            else:
                break
            start +=1
            # print(suf, start)
        suf = suf[::-1]
        # print(suf)
        # print(beg)
        middle = len(arr) - (len(suf) + len(beg))

        ans = 0
        ans = min(len(arr) - len(suf), len(arr) - len(beg))


        # print(ans)
        # ans = middle
        if len(suf) == len(beg) == len(arr):
            return 0
        else:
            for ind, val in enumerate(beg):
                x = bisect_left(suf, val)
                extra = x + ((len(beg) - ind)-1) + middle
                # print("Extra", extra)
                ans = min(ans,  extra)
                # print(val,x )
        
        return ans
