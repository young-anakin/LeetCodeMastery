class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cp = Counter(nums)
        for key, val in cp.items():
            if val >=2 :
                return key