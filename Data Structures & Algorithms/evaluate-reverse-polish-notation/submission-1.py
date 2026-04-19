class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        stack = []
        answer = 0
        
        def operation(op,num1,num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            if op == "/":
                return num1 / num2
            

        for element in tokens:
            if element not in operations:
                stack.append(int(element))
            else:
                answer = operation(element, stack[0], stack[1])
                stack[0] = answer
                stack.pop()
        
        return answer