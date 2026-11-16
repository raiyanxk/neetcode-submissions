class MinStack:

    def __init__(self):
        self.low = float('inf')
        self.mins = []
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.low = min(self.low, val)
        self.mins.append(self.low)

    def pop(self) -> None:
        top = self.stack.pop()
        self.mins.pop()
        if top == self.low:
            if self.mins:
                self.low = self.mins[-1]
            else:
                self.low = float('inf')

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
