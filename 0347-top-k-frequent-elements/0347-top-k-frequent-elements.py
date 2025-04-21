class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cp = Counter(nums)
        # storage for the elements
        bulk = []

        for key, val in cp.items():
            bulk.append((val, key))
        
        bulk.sort(reverse = True)
        # print(bulk)
        for i in range(k):
            ans.append(bulk[i][1])
        
        return ans