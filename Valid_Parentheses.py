s = "[(])"
parantheses = {"(": ")", "[": "]", "{": "}", "<": ">"}
stack = []
top = -1

for ele in s:
    if ele in ["(", "[", "{", "<"]:
        stack.append(ele)
        top += 1
    elif ele in [")", "]", "}", ">"]:
        if top >= 0 and parantheses[stack[top]] == ele:
            stack.pop()
            top -= 1
        else:
            stack.append(ele)
            break
print(stack)
if len(stack) == 0:
    print("True")
else:
    print("False")
