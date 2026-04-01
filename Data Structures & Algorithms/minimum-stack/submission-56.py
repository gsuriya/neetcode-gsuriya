class MinStack:
    """

    basically same as a normal stack, but know min at any time

    push
    - if not min_stack --> push it to both
    - if val < top of min_stack --> push it to both, else push to normal stack

    pop
    - if popping a minimum (top of min_stack) --> pop both

    """
    def __init__(self):
        self.stack = []
        self.min_stack = [] # stack of current minimums
        
    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



