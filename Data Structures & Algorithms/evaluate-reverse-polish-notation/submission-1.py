class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if (i != "+" and i != "-" and i != "*" and i != "/"):
                stack.append(i)
            elif (i == "+"):
                curr = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif (i == "-"):
                curr = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif (i == "*"):
                curr = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)
            elif (i == "/"):
                curr = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(curr)

        return int(stack[-1])