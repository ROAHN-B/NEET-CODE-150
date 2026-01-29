temperatures = [30, 38, 30, 36, 35, 40, 28]
stack = []
output = [0] * len(temperatures)


for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()
        output[stackInd] = i - stackInd
    stack.append([t, i])
print(output)
