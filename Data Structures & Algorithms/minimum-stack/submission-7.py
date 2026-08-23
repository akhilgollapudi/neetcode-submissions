class MinStack:

    def __init__(self):
        self.stack =[]
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]


    def getMin(self) -> int:
        if self.minStack:
            return int(self.minStack[-1])