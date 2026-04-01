class MinStack:
    # O(1) time for every function

    """

    stack = [
       -2 -2
    ]

    min_stack = [
        -2
    ]

    """
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        # if nothing in both stacks
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # if num being popped is the MIN
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
       
    def getMin(self) -> int:
        return self.min_stack[-1]

