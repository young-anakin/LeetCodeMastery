class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        mx = 0

        heaters.sort()
        # we did this so as to not cause an index out of bounds error
        # bisect_left gets us the >= value of houses[ind]
        heaters.append(10000000000000)
        for ind in range(len(houses)):
            val = bisect_left(heaters, houses[ind]) 
            temp = min(abs(heaters[val] - houses[ind]), abs(houses[ind] - heaters[val-1]))
            # min -> 10000000000000 - 5 or 5 - 2 -> 3
            mx = max(mx, temp)
            # range -> 1
            # range -> 3
        return mx