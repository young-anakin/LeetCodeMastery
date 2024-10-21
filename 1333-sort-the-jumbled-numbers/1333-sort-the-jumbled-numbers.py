class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dd = defaultdict(list)
        arr = set()
        for num in nums:
            num = str(num)
            val = ""
            for ind in num:
                val += str(mapping[int(ind)])
            dd[int(val)].append(int(num))
            arr.add(int(val))
        
        arr = list(arr)
        arr.sort()
        fin = []
        for ind in arr:
            tmp = dd[ind]
            fin.extend((tmp))
        return fin
                
