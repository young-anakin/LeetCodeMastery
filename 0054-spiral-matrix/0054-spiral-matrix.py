class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans  = []
        arr = matrix


        right = True
        down = False
        left = False
        up = False


        ind = 0
        j = 0

        top = 0
        bottom = 0
        sideL = 0
        sideR = 0
        print(len(matrix) * len(matrix[0]))
        for cp in range(len(matrix) * len(matrix[0])):
            if right:
                if j >= len(arr[0]) - sideR:
                    down = True
                    right = False
                    ind +=1
                    top +=1
                    j-=1
                else:
                    ans.append(arr[ind][j])
                    j +=1
                    
            if down:
                if ind >= len(arr) - bottom:
                    down = False
                    left = True
                    j -=1
                    sideR +=1
                    ind -=1
                else:
                    ans.append(arr[ind][j])
                    ind +=1

            if left:
                if j < 0 + sideL:
                    up = True
                    left = False
                    ind -=1
                    sideL +=1
                    j +=1
                else:
                    ans.append(arr[ind][j])
                    j -=1

            fl = False
            if up:
                if ind < 0 + top:
                    right = True
                    up = False
                    j +=1
                    bottom +=1
                    ind +=1
                    fl = True
                else:
                    ans.append(arr[ind][j])
                    ind -=1


            if fl and right:
                fl = False
                if j >= len(arr[0]) - sideR:
                    down = True
                    right = False
                    ind +=1
                    top +=1
                    j-=1
                else:
                    ans.append(arr[ind][j])
                    j +=1
        
        return ans




            
