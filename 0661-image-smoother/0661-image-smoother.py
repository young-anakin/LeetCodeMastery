class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def inbound(ind, j):
            return ind < len(img) and ind >= 0 and j < len(img[0]) and j >= 0

        
        new = [[0 for i in range(len(img[0]))] for ind in range(len(img))]
        print(new)
        neighbours = [(0,0), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        for ind in range(len(img)):
            for j in range(len(img[0])):
                sm = 0
                cp = 0
                for a, b in neighbours:
                    if inbound(ind+a, j+b):
                        # print(ind+a, j+b, len(img), len(img[0]))

                        cp +=1
                        sm += img[a+ind][j+b]
                
                new[ind][j] = int(math.floor(sm/cp))
        return new       