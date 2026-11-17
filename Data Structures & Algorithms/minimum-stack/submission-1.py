class MinStack:

    def __init__(self):
        self.nums = []
        self.mins = []
        self.small = float('inf')    

    def push(self, val: int) -> None:
        self.small = min(self.small, val)
        self.mins.append(self.small)
        self.nums.append(val)

    def pop(self) -> None:
        self.nums.pop()
        self.mins.pop()
        
        if not self.mins:
            self.small = float('inf')
        else:
            self.small = self.mins[-1]

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.mins[-1]
