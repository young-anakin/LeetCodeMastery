class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        mn = float("inf")
        mx = float("inf") * -1

        def is_prime(num):
            # Handle edge cases
            if num <= 1:
                return False  # 0 and 1 are not prime numbers
            if num <= 3:
                return True  # 2 and 3 are prime numbers
            if num % 2 == 0 or num % 3 == 0:
                return False  # Exclude multiples of 2 or 3

            # Check divisors from 5 to sqrt(num)
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6  # Skip even numbers and multiples of 3

            return True
        arr = []
        for ind, val in enumerate(nums):
            if is_prime(val):
                arr.append(ind)
        
        # print(arr)
        return abs(arr[0] - arr[-1])

