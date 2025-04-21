class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # store as tuples the key, value pairs of the values

        organized = []
        for val in strs:
            word = [i for i in val]
            word.sort()
            organized.append((val, tuple(word)))

        # print(organized)

        cp = defaultdict(list)
        
        for a, b in organized:
            cp[b].append(a)
        
        ans = []
        for key, val in cp.items():
            ans.append(val)
        
        return ans