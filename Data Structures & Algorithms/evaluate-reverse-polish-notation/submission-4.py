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
    
        
        return int(stack[-1])