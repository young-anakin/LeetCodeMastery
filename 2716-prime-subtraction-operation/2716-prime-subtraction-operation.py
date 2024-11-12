class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
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
        for ind in range(2, 1001):
            if is_prime(ind):
                primes.append(ind)
        
        ans = []
        ss = set()
        ss.add(-1)
        # print(primes)

        nums = nums[::-1]
        for ind in nums:
            if not ans:
                ans.append(ind)
            else:
                if ind < ans[-1]:
                    ans.append(ind)
                else:
                    fl = False
                    sub = abs(ans[-1] - ind) + 1

                    x = bisect_left(primes, sub)
                    # print(sub, x)
                    if x >= len(primes):
                        return False
                    if ind - primes[x] <= 0:
                        return False
                    ans.append(ind- primes[x])
                    # if x not in
        ans = ans[::-1]
        first = ans[0]
        for ind in range(1, len(ans)):
            if first == ans[ind] or first > ans[ind]:
                return False
            first = ans[ind]
        
        
        # print(ans)
        return True