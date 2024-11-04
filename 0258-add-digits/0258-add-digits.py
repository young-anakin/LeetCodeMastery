class Solution:
    def addDigits(self, num: int) -> int:
        arr = []
        for ind in str(num):
            arr.append(ind)

        def calc(arr):
            if len(arr) == 1:
                return int(arr[0])
            

            ans = 0
            for ind in arr:
                ans += int(ind)
            arr = []
            for ind in str(ans):
                arr.append(ind)
            
            return calc(arr)
        
        return calc(arr)
            
