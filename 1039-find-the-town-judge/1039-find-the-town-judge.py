class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # Town Judge :
        # Trusts Nobody
        # Everybody Trusts him


        # How many people a person trusts
        truster = defaultdict(int)
        # How many people trusts the person
        trustee = defaultdict(int)

        for p1, p2 in trust:
            truster[p1] +=1
            trustee[p2] +=1
        
        for i in range(1, n+1):
            if truster[i] == 0 and trustee[i] == n-1:
                return i
        
        return -1
