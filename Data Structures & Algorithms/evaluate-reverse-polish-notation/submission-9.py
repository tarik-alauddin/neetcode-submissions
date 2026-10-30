class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-/*":
                right, left = stack.pop(), stack.pop()

                if token == "+":
                    res = left + right
                elif token == "-":
                    res = left - right
                elif token == "*":
                    res = left * right
                elif token == "/":
                    res = int(left/right)

                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]