class MinStack:
    def __init__(self):
        self.stack = []
        self.min_tracker = []  # current min is min_tracker[-1]

    def push(self, val: int) -> None:
        # push onto the stack
        self.stack.append(val)

        # update min tracker
        # first number added by default
        if not self.min_tracker:
            self.min_tracker.append(val)
        # if val <= min
        elif self.min_tracker and val <= self.min_tracker[-1]:
            self.min_tracker.append(val)


    def pop(self) -> None:
        # edge case nothing in stack
        if not self.stack:
            return None

        # pop from stack
        popped = self.stack.pop()
        # if popped was current min, pop from min_tracker
        if popped == self.min_tracker[-1]:
            self.min_tracker.pop()
        
    def top(self) -> int:
        # edge case: nothing in stack
        if not self.stack:
            return None
        return self.stack[-1]
       
    def getMin(self) -> int:
        # edge case min_tracker empty
        if not self.min_tracker:
            return None
        return self.min_tracker[-1]
        
        



   
   
   
    # gpt says my code should work, but when I put it in VSC it doesn
    # only thing i did wrong was use min variable which was unneeded sure
    # but idk why that causes so many issues

    # push
    # pop
    # top (peek)
    # getMin gets min element

    """
    Class Structure: all O(1) methods
     X OUT ------Therefore, stack elems should be added in descending order

    5 6 3 6 0 8 1
    stack =  [5, 6]
    Way to dynamically track the min element as elems added to stack?

    min = 3
    min_tracker = [5]

    instance fields:
        min (int)
        min_tracker (stack)
        stack (stack)

    def push:
        if min changes --> add to min_tracker
    
    def pop
        stack.pop()
        if min popped from stack:
            min_tracker.pop()
            min = min_tracker.peek()

    def getMin()
        min_tracker[-1]

    def top()
        return stack[-1]

    """

    """
    def __init__(self):
        self.stack = []
        self.min_tracker = []
        self.minimum = 999999999
       
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum = val
            self.min_tracker.append(self.minimum)

    def pop(self) -> None:
        if not self.stack:
            return None
            
        popped = self.stack.pop()
        if popped == self.minimum:
            self.min_tracker.pop()
            if self.min_tracker:
                self.minimum = self.min_tracker[-1]
            else:
                self.minimum = 999999999


    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
    """

