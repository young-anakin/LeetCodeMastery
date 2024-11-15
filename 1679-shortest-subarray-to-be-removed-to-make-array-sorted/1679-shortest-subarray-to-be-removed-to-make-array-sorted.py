class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        stack = [arr[0]]
        start = 1
        beg = stack

        while start < len(arr):
            if arr[start] >= stack[-1]:
                stack.append(arr[start])
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
        
        suf = suf[::-1]

        middle = len(arr) - (len(suf) + len(beg))

        ans = min(len(arr) - len(suf), len(arr) - len(beg))

        if len(suf) == len(beg) == len(arr):
            return 0
        else:
            for ind, val in enumerate(beg):
                x = bisect_left(suf, val)
                extra = x + ((len(beg) - ind)-1) + middle
                ans = min(ans,  extra)
        
        return ans
