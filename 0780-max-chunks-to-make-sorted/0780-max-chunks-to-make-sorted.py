class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cp = 0
        stack = []

        for ind in range(0, len(arr)):
            stack.append(arr[ind])

            if ind == max(stack):
                cp +=1
                stack = []
        
        return cp


