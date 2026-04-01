class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # bro i saw a yt short for this question on accident
        stack = []

        for s in tokens:
            # for operations, take last two numbers in stack and perform op,
            # add res back to stack
            if s == "+":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1+ val2
                    stack.append(res)
            elif s == "-":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 - val1
                    stack.append(res)
            elif s == "*":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1 * val2
                    stack.append(res)
            elif s == "/":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = int(val2 / val1)
                    stack.append(res)
            else: # append ints
                stack.append(int(s))
        
        return stack[-1]