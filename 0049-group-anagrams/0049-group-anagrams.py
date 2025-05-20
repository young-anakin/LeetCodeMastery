class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        new = []

        for word in strs:
            tmp = [i for i in word]
            tmp.sort()
            tmp = "".join(tmp)
            new.append((tmp, word))
        
        dd = defaultdict(list)
        print(new)
        for word in new:
            dd[word[0]].append(word[1])
        

        ans = [val for val in dd.values()]
        return ans