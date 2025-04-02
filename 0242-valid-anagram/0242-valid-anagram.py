class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cp = Counter(s)
        cp2 = Counter(t)

        if cp == cp2:
            return True
        
        return False