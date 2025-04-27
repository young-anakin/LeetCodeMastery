class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        ans = []
        for ind in stack:
            if ind == "..":
                if ans:
                    ans.pop()
            else:
                if ind != "" and ind != '/' and ind != ".":
                    ans.append(ind)
                else:
                    continue
            # ans.append("/")
        if not ans: 
            return "/"
        print(ans)
        truth = ""
        for ind in ans:
            truth += "/"
            truth += ind
        return truth
        # if not ans:
        #     return "/"
        # return 


