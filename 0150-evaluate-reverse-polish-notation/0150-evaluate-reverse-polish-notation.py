from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def mult(x, y):
            return x * y

        def div(x, y):
            return int(x / y)

        def sub(x, y):
            return x - y

        def add(x, y):
            return x + y
        
        operation = {'+':add,'-':sub,'*':mult,'/':div}
        operators = '+-*/'
        stack = deque()

        for token in tokens:
            if token in operators:
                rightOperand, leftOperand = stack.pop(), stack.pop()
                stack.append(operation[token](leftOperand, rightOperand))
            else:
               stack.append(int(token))

        return stack.pop()