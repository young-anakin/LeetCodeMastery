class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        dd = defaultdict(int)
        ans = set()
        
        for val in folder:
            tmp = ""
            if val.count("/") == 1:
                ans.add(val)
            else:
                cp = 0
                fl = True
                for ind in val:
                    if ind == "/":
                        if cp == 0:
                            cp +=1
                            tmp += ind
                        else:
                            if tmp in ans:
                                fl = False
                                break
                            else:
                                tmp += ind
                    else:
                        tmp += ind
                
                if fl:
                    ans.add(tmp)
        

        return list(ans)

                    # tmp += ind


