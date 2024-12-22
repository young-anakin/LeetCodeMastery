class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
       result=[]
       dd=defaultdict(int)
       p_count=Counter(p)
       ss=len(s)
       k=len(p)
       for i in range(ss):
         dd[s[i]]+=1
         if i>=k-1:
            if p_count==dd:
                result.append(i-(k-1))
            if dd[s[i-(k-1)]]==1:
                del dd[s[i-(k-1)]]
            else:
                dd[s[i-(k-1)]]-=1
       return result