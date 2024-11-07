class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        arr = []
        for ind in candidates:
            arr.append(bin(ind)[2:])
        mn = 0
        for ind in arr:
            mn = max(mn, len(ind))
        
        ans = []
        for ind in arr:
            x = ""
            for j in range(len(ind), mn):
                x += "0"
            
            x += ind 
            ans.append(x)
        
        dd = defaultdict(int)
        fin = [0 for _ in range(mn)]
        for ind in ans:
            for j in range(len(ind)):
                if ind[j] == "1":
                    fin[j] +=1


        return max(fin)

        