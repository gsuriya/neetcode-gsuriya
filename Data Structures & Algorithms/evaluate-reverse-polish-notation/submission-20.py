class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """

        add all the other numbers to the stack
        if hit an operation, then do it w/ the 2 numbers the stack and push result

        """
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            elif c == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif c == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            
            else: # just a number
                stack.append(int(c))
        
        return stack[0]