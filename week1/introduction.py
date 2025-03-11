def operation():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operation = input("Enter the operation to perform (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
            return False
    else:
        print("Invalid operation")
        return False
    print(f'The result of {num1} {operation} {num2} is {result}')
    return True

operation()
