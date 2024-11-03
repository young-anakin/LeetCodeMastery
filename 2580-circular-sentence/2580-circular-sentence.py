class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = list(map(str, sentence.split(" ")))
        first = arr[0][-1]
        fl = True
        for i in range(1, len(arr)):
            if first == arr[i][0]:
                first = arr[i][-1]
                continue
            else:
                return False
        
        if arr[0][0] != arr[-1][-1]:
            return False

        return True