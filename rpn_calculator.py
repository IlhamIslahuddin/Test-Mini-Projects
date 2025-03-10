def rpn_calculator(expression):
    stack = []
   
    # Split the expression into tokens
    tokens = expression.split()
   
    for token in tokens:
        if token in "+-*/":

            b = stack.pop()
            a = stack.pop()
           
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b != 0:
                    stack.append(a / b)
                else:
                    return "Error: Division by zero"
        else:
            try:
                stack.append(float(token))
            except ValueError:
                return f"Error: Invalid token '{token}'"
   
    # The final result should be the only item left on the stack
    if len(stack) == 1:
        return stack.pop()
    else:
        return "Error: Invalid RPN expression"

if __name__ == "__main__":
    expression = "3 4 + 2 * 7 /"
    result = rpn_calculator(expression)
    print("Result:", result)
