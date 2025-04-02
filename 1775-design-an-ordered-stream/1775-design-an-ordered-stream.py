class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.arr = [0] * n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        if self.arr[self.ptr] == 0:
            return []
        else:
            i = 0
            ans = []
            for i in range(self.ptr, len(self.arr)):
                if self.arr[i] == 0:
                    break
                ans.append(self.arr[i])
            
            self.ptr = i
            return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)