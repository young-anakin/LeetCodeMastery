class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for ind in range(n+1):
            arr.append(bin(ind).count("1"))
        
        return(arr)