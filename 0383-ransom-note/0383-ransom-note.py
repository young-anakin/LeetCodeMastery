class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)

        for ind in magazine:
            mag[ind] +=1
        
        for ind in ransomNote:
            if mag[ind] != 0:
                mag[ind] -=1
            else:
                return False
        
        return True