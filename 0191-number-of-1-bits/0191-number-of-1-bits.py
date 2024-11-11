class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        return x.count('1')