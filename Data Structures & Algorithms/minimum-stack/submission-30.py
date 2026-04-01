class MinStack:
    def __init__(self):
        self.stack = []
        self.min_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_tracker or val <= self.min_tracker[-1]:
            self.min_tracker.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.min_tracker[-1]:  # Only pop min_tracker if it was the min
            self.min_tracker.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_tracker:
            return None
        return self.min_tracker[-1]