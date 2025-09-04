class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        


        # Knapsack ( one turn , we take . Another turn, we leave) -> Take it or leave it
        ans = 0
        memo = defaultdict(int)

        def dp(ind, curr_amount):
            # Base case

            if curr_amount > amount:
                return 0
            if ind >= len(coins):
                return 0
            
            if curr_amount == amount:
                return 1
            if (ind, curr_amount) not in  memo:
                memo[(ind, curr_amount)] = dp(ind, curr_amount + coins[ind]) + dp(ind+1, curr_amount) 

            return memo[(ind, curr_amount)]
        return dp(0, 0)
