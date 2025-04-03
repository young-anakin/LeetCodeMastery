class MinStack:

    def __init__(self):
        # this array simulates our stack
        self.stack = []
        # this array will be used to get the work for the minimum element
        self.minstack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.stack.pop()
            self.minstack.pop()
        else:
            self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()