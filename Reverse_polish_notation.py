tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
stack = []

for ele in tokens:
    if ele not in ["+", "-", "/", "*"]:
        stack.append(int(ele))
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if ele == "+":
            stack.append(int(num1 + num2))
        elif ele == "-":
            stack.append(int(num1 - num2))
        elif ele == "/":
            stack.append(int(num1 / num2))
        elif ele == "*":
            stack.append(int(num1 * num2))
print(stack[0])
