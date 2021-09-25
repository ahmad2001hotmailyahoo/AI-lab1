def calculator():
    first = int(input("Enter the first number\n"))
    seconed = int(input("Enter the seconed number\n"))
    operation = input("Enter the operator + , - / , * ,%, ^\n")
    if operation == '+':
        return first + seconed
    elif operation == '*':
        return first * seconed
    elif operation == '/':
        return first / seconed
    elif operation == '-':
        return first - seconed
    elif operation == '^':
        return first ^ seconed
    elif operation == '%':
        return first % seconed
    else:
        return "not a valid operator"

print(calculator())