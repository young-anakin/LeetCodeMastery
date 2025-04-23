class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        array = [0 for _ in range(n)]
        if n == 1:
            return [0 for _ in range(len(queries))]
        cp = 0
        ans = []
        for i, j in queries:

            if i == 0:
                if array[i+1] == array[i] and (array[i+1] != 0):
                    cp -=1
                array[i] = j
                if array[i] == array[i+1]:
                    cp +=1
            elif i == n-1:
                if array[i-1] == array[i] and (array[i] != 0):
                    cp -=1
                array[i] = j
                if array[i] == array[i-1]:
                    cp +=1
            else:
                if array[i+1] == array[i] and (array[i] != 0):
                    cp -=1
                if array[i-1] == array[i] and (array[i] != 0):
                    cp -=1
                array[i] = j
                if array[i] == array[i-1]:
                    cp +=1
                if array[i] == array[i+1]:
                    cp +=1

            ans.append(cp)

            # ans.append()
        return ans
