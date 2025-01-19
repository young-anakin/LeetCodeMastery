from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowChecker = {}
        # x = Counter()
        for a in range(0, len(board)):
            y = Counter(board[a])
            for key, values in y.items():
                if values > 1:
                    if key != '.':
                        return False
        for b in range(0, len(board)):
            li = []
            for c in range(0, len(board)):
                if board[c][b] in li:
                    return False
                if board[c][b] != ".":
                    li.append(board[c][b])
        cp = 0
        xy = 0
        bs= []

        for ind in range(0, 3):
            for a in range(0, 3):
                li = []
                for b in range(0, 3):
                    li.append(board[xy + b][cp:cp + 3])
                bs.append(li)
                cp += 3
                # print(bs)




            cp = 0
            xy += 3
        # print(bs[0])
        # print(bs[7][1][0])
        for time in range(0, 9):
            x = set()
            for i in range(0, 3):
                for j in range(0, 3):

                    if bs[time][i][j] == ".":
                        continue
                    else:
                        if bs[time][i][j] in x:
                            print(bs[time])
                            return False
                        else:
                            x.add(bs[time][i][j])
        return True
                    