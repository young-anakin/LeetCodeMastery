class Solution:
    def invalidTransactions(self, trans: List[str]) -> List[str]:
        dicto = defaultdict(list)
        
        
        for i in trans:
            data = list(map(str,i.split(",")))
            dicto[data[0]].append([data[1],data[2],data[3]])

        res = []
        
        for i in dicto:
            for j in range(len(dicto[i])):
                if int(dicto[i][j][1]) > 1000:
                    res.append(",".join([i,dicto[i][j][0],dicto[i][j][1],dicto[i][j][2]]))
                else:
                    for k in range(len(dicto[i])):
                        if len(dicto[i])>1:
                            if abs(int(dicto[i][j][0]) - int(dicto[i][k][0])) <= 60 and dicto[i][j][2] != dicto[i][k][2]:
                                res.append(",".join([i,dicto[i][j][0],dicto[i][j][1],dicto[i][j][2]]))
                                break
        return res