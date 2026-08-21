class MinStack:
    """
    
    normal stack, get min at any time

    mins = [-2]

    stack = [-2]

    """

    def __init__(self):
        self.stack = []
        self.mins = [] # stack as well
        
    def push(self, val: int) -> None:
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        # if the one you pop is the current min, pop from both stacks
        val = self.stack.pop()

        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
