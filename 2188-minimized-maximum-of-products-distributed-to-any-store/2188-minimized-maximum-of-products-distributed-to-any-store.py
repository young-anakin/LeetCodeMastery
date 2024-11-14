class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        mn = 0
        mx = max(quantities)
        def BinarySearch(left, right):
            while left < right:
                md = (left + right) // 2
                # print(left, right, md)  # Debug print
                if canDistribute(md):
                    right = md  # Narrow down to the left side
                else:
                    left = md + 1  # Narrow down to the right side

            return right  # Or `right`
        def canDistribute(k):
            cp = 0
            for ind in range(len(quantities)):
                cp += math.ceil(quantities[ind]/k)
            
            if cp <= n:
                return True
            else:
                return False
        # print((mn + mx)//2)
        return BinarySearch(1, mx)

        