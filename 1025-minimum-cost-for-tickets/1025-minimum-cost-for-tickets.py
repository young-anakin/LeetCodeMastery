class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)

        mx = max(days)

        def dp(i):
            if i > mx:
                return 0

            sub = float("inf")
            if i not in days:
                # print(i, ans)
                memo[i] = dp(i+1)

            if i not in memo:
                
                for a, b in enumerate(costs):
                    if a == 0:
                        sub = dp( i + 1) + b
                    elif a == 1:
                        sub = min(sub, dp(i + 7) + b)
                    else:
                        sub = min(sub, dp(i + 30) + b)
                memo[i] = sub

            return memo[i]
        
        val = dp(days[0])
    
        # print(memo)
        return val