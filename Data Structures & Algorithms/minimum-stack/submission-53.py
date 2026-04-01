class MinStack:
    """

    stack = [
        1 3 0 0 4
    ]

    min_stack = [
        1 0
    ]

    when pushing onto stack, if val is <= than current min (min_stack[-1])
    then append to min stack

    when popping, if popping the min val (stack.pop() = min_stack[-1])
    then also pop from the min_stack


    """
    def __init__(self):
        self.stack = []
        self.min_stack = [] # tracks mins throughout the stack
                            # self.min_stack[-1] is current min

    def push(self, val: int) -> None:
        self.stack.append(val)
        # append new min too
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val) 

    def pop(self) -> None:
        popped = self.stack.pop()
        # if you popped the current min
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        