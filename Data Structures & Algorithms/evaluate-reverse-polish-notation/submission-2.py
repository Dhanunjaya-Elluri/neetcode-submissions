class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                top = stack.pop()
                bot = stack.pop()
                if token == '+':
                    res = bot + top
                    stack.append(res)
                elif token == '-':
                    res = bot - top
                    stack.append(res)
                elif token == '*':
                    res = bot * top
                    stack.append(res)
                else:
                    res = int(bot / top)
                    stack.append(res)
        return stack[0]
        