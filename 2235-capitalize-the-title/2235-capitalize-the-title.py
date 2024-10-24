class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []

        tt = list(map(str, title.split(" ")))

        for ind in tt:
            temp = ind.lower()
            if len(temp) <= 2:
                ans.append(temp)
            else:
                temp = temp[0].upper() + temp[1:]
                ans.append(temp)
        
        return " ".join(ans)
        print(tt)
