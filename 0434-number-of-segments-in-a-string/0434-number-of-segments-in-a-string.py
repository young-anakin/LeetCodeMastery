class Solution:
    def countSegments(self, s: str) -> int:
        ans = s.split(" ")
        sec = 0
        while ans:
            if ans[-1] != "":
                sec +=1 
            ans.pop()
        return sec