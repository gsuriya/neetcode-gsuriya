class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        
        truncate towards 0 --> so use int() not //

        """

        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                divisor = stack.pop()
                stack.append(int(stack.pop() / divisor))
            else:
                stack.append(int(c))

        return stack[0]







