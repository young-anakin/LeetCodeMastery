class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for ind in range(1, (numRows)+1):
            tmp = [0 for _ in range(ind)]
            tmp[0] = 1
            tmp[-1] = 1
            ans.append(tmp)
        ans[0][0] = 1
        for ind in range(1, (numRows)):
            for j in range(1, len(ans[ind])-1):
                if ans[ind][j] != 1:
                    # print(ind, j)
                    # pass
                    ans[ind][j] = ans[ind-1][j-1] + ans[ind-1][j]

        print(ans)
        return ans
