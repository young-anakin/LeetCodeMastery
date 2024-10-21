class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)

    def backtrack(self, s, start, ss):
        if start == len(s):
            return 0

        max_count = 0

        for end in range(start+1, len(s)+1):
            sub_str = s[start:end]
            if sub_str not in ss:
                ss.add(sub_str)
                max_count = max(max_count, 1+ self.backtrack(s, end, ss))
                ss.remove(sub_str)
        
        return max_count

        

            


