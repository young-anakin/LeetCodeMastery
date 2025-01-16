class Solution(object):
    def sortColors(self, arr):
        
        for a in range(0, len(arr)):
            min = a
            for b in range(a+1, len(arr)):
                if arr[min] > arr[b]:
                    min = b
            arr[min], arr[a] = arr[a], arr[min]
        return arr