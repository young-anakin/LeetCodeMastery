class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dd = Counter(arr)
        for i, ind in enumerate(arr):
            if ind * 2 in arr[0:i] or ind *2 in arr[i+1:]:
                print(ind)
                return True
        
        return False