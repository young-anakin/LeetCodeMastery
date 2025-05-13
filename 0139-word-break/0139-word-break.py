class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        i = 0
        j = 0

        memo = defaultdict(bool)


        def dp(i, j):
            if (i, j) not in memo:
                if i >= len(s) or j >= len(s):
                    if s[i:j] in wordDict:
                        return True
                    return False

                if s[i:j] in wordDict:

                    memo[(i, j)] =  dp(i, j+1) or dp(j, j+1)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = dp(i, j+1)
                    return memo[(i, j)]
            
            return memo[(i, j)]
        
        # print(dp(0, 0))
        return dp(0, 0)