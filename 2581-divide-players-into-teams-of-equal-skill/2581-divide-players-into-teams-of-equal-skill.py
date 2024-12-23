class Solution:
    def dividePlayers(self, a: List[int]) -> int:
        a = sorted(a)
        optimal = a[0] + a[-1]
        left = 0
        right = len(a) - 1
        result = 0
        while left < right:
            if not a[left] + a[right] == optimal:
                return -1
            result += a[left] * a[right]
            left += 1
            right -= 1
        return result   