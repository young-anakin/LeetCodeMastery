class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = []

        mxArr = []

        items.sort()
        mn = -1
        for ind in range(len(items)):
            mn = max(mn, items[ind][1])
            mxArr.append(mn)

        
        itemsBeauty = []
        for ind in items:
            itemsBeauty.append(ind[0])
        for ind in queries:
            x = bisect_right(itemsBeauty, ind)
            # print(x)
            if x == 0:
                ans.append(0)
                continue
            ans.append(mxArr[x-1])
        
        # print(items)
        # print(mxArr)
        return ans