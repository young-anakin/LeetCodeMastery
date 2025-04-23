class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        cp = 0
        dd = defaultdict(int)
        count = 0
        mx = 0
        while j < len(fruits):  
            
            if dd[fruits[j]] == 0:
                cp +=1
            dd[fruits[j]] +=1
            while cp > 2:
                dd[fruits[i]] -=1
                if dd[fruits[i]] == 0:
                    cp -=1
                count -=1
                i +=1
            count +=1
            mx = max(mx, count)
            j +=1
        
        return mx
