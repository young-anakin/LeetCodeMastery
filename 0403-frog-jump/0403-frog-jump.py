class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dd = defaultdict(set)
        dd[0].add(0)

        ss = set()
        for ind in stones:
            ss.add(ind)
        
        dir = [-1, 0 , 1]
        for stone in stones:
            for jump in dd[stone]:
                for d in [jump-1, jump+1, jump]:
                    if d > 0 and stone + d in ss:
                        dd[stone + d].add(d)
        
        return len(dd[stones[-1]]) > 0