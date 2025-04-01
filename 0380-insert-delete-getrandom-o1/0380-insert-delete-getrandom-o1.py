class RandomizedSet:

    def __init__(self):
        self.values = list()
        self.location = defaultdict(int)
        # self.curr = 

    def insert(self, val: int) -> bool:
        if val not in self.location:
            self.values.append(val)
            self.location[val] = len(self.values)-1
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        else:
            first, second = self.location[val], -1
            self.values[first], self.values[second] = self.values[second], self.values[first]

            self.location[self.values[first]] = first
            del self.location[self.values[second]]
            self.values.pop()

            return True


    def getRandom(self) -> int:
        randNum = randint(0, len(self.values)-1)
        return self.values[randNum]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()