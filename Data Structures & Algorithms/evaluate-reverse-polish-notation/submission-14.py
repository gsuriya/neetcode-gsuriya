class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            # if operator, then pop from stack until empty and push result
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                stack.append(-1*stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            # else: its a number, add to stack
            else:
                stack.append(int(c))
        
        return stack.pop()
                