class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opens = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for c in s:
            if c not in opens:
                stack.append(c)
            elif not stack or stack[-1] != opens[c]:
                return False
            else:
                stack.pop()





        return len(stack) == 0