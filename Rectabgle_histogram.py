heights = [7, 1, 7, 2, 2, 4]
res = 0
stack = []

for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][1] > h:
        index, height = stack.pop()
        res = max(res, height * (i - index))
        start = index
    stack.append((start, h))

for i, h in stack:
    res = max(res, h * (len(heights) - i))
print(res)
