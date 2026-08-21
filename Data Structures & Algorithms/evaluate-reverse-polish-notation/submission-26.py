class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                stack.append(int(second / first))

            else:
                stack.append(int(c))
        
        return stack[-1]