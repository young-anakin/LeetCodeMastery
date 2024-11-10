class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        x = (math.sqrt(area))
        # print(x)
        if int(x) == x:
            return [int(x), int(x)]
        for ind in range(int(x), 0, -1 ):
            # print(ind, area/ind)
            if int(area/ind) == area/ind:
                return [max(int(area/ind), ind), min(int(area/ind), ind)]


        return []
