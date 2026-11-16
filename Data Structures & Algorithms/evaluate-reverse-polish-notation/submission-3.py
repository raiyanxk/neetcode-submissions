class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        for t in tokens:
            if t in ops:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(ops[t](op1, op2))
            else:
                stack.append(int(t))
        
        while len(stack) > 1:
            t = stack.pop()
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(ops[t](op1, op2))
            else:
                stack.append(t)
        
        return int(stack[-1])