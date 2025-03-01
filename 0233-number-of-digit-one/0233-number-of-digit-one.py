class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        i = 1
        while i <= n:
            divider = i * 10
            countr += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return countr