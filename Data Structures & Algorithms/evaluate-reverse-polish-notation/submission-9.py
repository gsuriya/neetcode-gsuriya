class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """

        stack = [

            /
            4
            9
        ]

        """

        stack = []

        for c in tokens:
            if c == "+":
                sum_ = stack.pop() + stack.pop()
                stack.append(sum_)
            elif c == "-":
                diff = -(stack.pop() - stack.pop())
                stack.append(diff)
            elif c == "*":
                product = stack.pop() * stack.pop()
                stack.append(product)
            elif c == "/":
                first = stack[-2]
                second = stack.pop()
                stack.pop()
                stack.append(int(first/second))
            else: # c is an integer
                stack.append(int(c))
        
        return stack[-1]