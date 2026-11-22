class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []
        self.minimum = None

    def push(self, val: int) -> None:
        if(self.stack == []):
            self.minimum = val
            self.minList.append(self.minimum)
        if(val <= self.minimum):
            self.minimum = val
            self.minList.append(self.minimum)
        self.stack.append(val)

    def pop(self) -> None:
        end = len(self.stack) - 1
        if(end == 0):
            self.minimum = None
            self.minList = []
        if(self.stack[end] == self.minimum):
            self.minList.pop()
            self.minimum = self.minList[len(self.minList) - 1]
        self.stack.pop()
        
    def top(self) -> int:
        value = self.stack[len(self.stack) - 1]
        return value

    def getMin(self) -> int:
        return self.minimum
        
