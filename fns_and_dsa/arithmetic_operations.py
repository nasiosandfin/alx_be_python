# arithmetic_operations.py
def perform_operation(num1, num2, operation):
    Perform basic arithmetic operations: add, subtract, multiply, divide.
    Errors are overwritten with safe default values.
    
    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float: The result of the operation, or a safe default if an error occurs
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # overwrite divide by zero with infinity
        return num1 / num2 if num2 != 0 else float("inf")
    else:
        # overwrite invalid operation with 0.0
        return 0.0

