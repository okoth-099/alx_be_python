def perform_operation(num1, num2, operation):
    if perform_operation == "add":
        return num1 + num2
    if perform_operation == "subtract":
        return num1 - num2
    if perform_operation == "multiply":
        return num1 * num2
    if perform_operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        elif num > 0:
            return num1 / num2
        else:
            return "Operation does not exist"
    else:
        "Operation does not exist"
