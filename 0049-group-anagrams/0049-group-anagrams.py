class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dd = defaultdict(list)
        for val in strs:
            ss = []
            for i in val:
                ss.append(i)
            ss.sort()
            dd[*ss].append(val)
        for key, values in dd.items():
            ans.append(values)
        
        return ans