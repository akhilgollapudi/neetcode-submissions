import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalRPNStack = []
        operators = ["+","-","*","/"]
        operators = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.truediv
        }
        for token in tokens:
            
            if token in operators:
                right = evalRPNStack.pop()
                left = evalRPNStack.pop()
                action = operators[token]
                result = action(left,right)
                evalRPNStack.append(int(result))
            else:
                evalRPNStack.append(int(token))
        return evalRPNStack[-1]
