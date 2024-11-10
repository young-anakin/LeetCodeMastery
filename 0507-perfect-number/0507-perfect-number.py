class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Function to check if a number is prime
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        if is_prime(num):
            return False
        
        if num == 1:
            return False
        if num == 2:
            return False
        mn = 0
        for ind in range(2, num):
            if num%ind == 0:
                mn = ind
                break
        
        mn = int(num/mn)
        # ans = [1, mn]
        ans = []
        for ind in range(1, mn+1):
            if num%ind == 0:
                ans.append(ind)
        if sum(ans) == num:
            return True
        return False

