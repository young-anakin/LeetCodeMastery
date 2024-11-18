class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        arr = []
        arr.extend(code)
        arr.extend(code)
        print(arr)
        ans = []
        for ind in range(len(code)):
            if k > 0:
                sm = 0
                for j in range(ind+1, ind + k +1):
                    sm += arr[j]
                ans.append(sm)
            elif k == 0:
                ans.append(0)
            else:
                # print("YO", ind+len(code)-1, (ind+len(code)-1) + k)
                sm = 0
                for j in range(ind+len(code)-1, (ind+len(code)-1)+k, -1):
                    # print(arr[j])
                    sm += arr[j]
                ans.append(sm)
        
        return (ans)