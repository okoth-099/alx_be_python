def perform_operation(num1, num2, operation):
    if perform_operation == "add":
        return num1 + num2
    if perform_operation == "subtract":
        return num1 - num2
    if perform_operation == "multiply":
        return num1 * num2
    if perform_operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionErrror:
            return "Error: Cannot divide by zero!"
    else:
        "Operation does not exist"
